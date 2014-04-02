from defines import *
from movie import *
from model import *
from util import *
from questions import *
from anketePoints import *

import os
import urllib
import re
import logging
import jinja2
import webapp2

from google.appengine.runtime import DeadlineExceededError
from google.appengine.api import mail
from google.appengine.runtime import apiproxy_errors


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class IntroPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'last': self.request.get('last'),
        }
        template = JINJA_ENVIRONMENT.get_template('intro.html')
        self.response.write(template.render(template_values))

def isEmailValid( email ):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    
def getUnenteredMsg( value ):
    return ERROR_NOT_ENTERED % (labels[ value ],)              # toto test
    
def hasAccomodationRight(workplace):
    return workplace in workplacesWithAcc
    
class MainPage(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'workplaces': workplaces,
            'orderedWorkplaces': orderedWorkplaces,
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        
    def get(self):
        self.displayPage()
           
    def saveToSession(self, empl):
        self.session[FIRST_NAME] = empl.firstname
        self.session[LAST_NAME] = empl.lastname
        self.session[EMAIL] = empl.email
        self.session[EMPLOYER] = empl.employer
        self.session[WORKPLACE] = empl.workplace
        self.session[ACCOMODATION] = empl.accomodation
        self.session[RESIDENCE] = empl.residence
        self.session[ROOMMATE] = empl.roommate
        
    def validateEmail(self, email, errors):
        if not email:
            errors.append( getUnenteredMsg( EMAIL ))
            return
        
        if not isEmailValid(email):
            errors.append( ERROR_EMAIL_INVALID )
            return
        
        key = ndb.Key(EmployeeEntity, email)
        if exist(key):
            errors.append( ERROR_EMAIL_EXIST )
            return
        
        return key
                    
    #todo using employee
    def validateData(self):
        errors = []
        errorIds = []
        
        if not self.request.get('firstname'):
            errors.append( getUnenteredMsg( FIRST_NAME ))
            errorIds.append('firstname')
            
        if not self.request.get('lastname'):
            errors.append( getUnenteredMsg( LAST_NAME ))
            errorIds.append('lastname')
            
        key = self.validateEmail( self.request.get('email'), errors )
        if not key:
            errorIds.append('email')
                   
        if not self.request.get('employer'):
            errors.append( getUnenteredMsg( EMPLOYER ))
            errorIds.append('employer')
            
        workplace = self.request.get('workplace')
        if not workplace:
            errors.append( getUnenteredMsg( WORKPLACE ))
            errorIds.append('workplace')
            
        if workplace != 'BA':                                           #todo extract fn
            if ( self.request.get('accomodation') ):
                if not self.request.get('residence'):
                    errors.append( getUnenteredMsg( RESIDENCE ))
                    errorIds.append('residence')
                    
                if not self.request.get('roommate'):
                    errors.append( getUnenteredMsg( ROOMMATE ))
                    errorIds.append('roommate')
        
        return (errors, errorIds, key)
            
            
    def post(self):
        errors, errorIds, key = self.validateData() 
        if errors:
            self.displayPage( self.request.params, errors, errorIds )
            return
        
        email = self.request.get('email')
        logging.info('employee: ' + email)
        
        empl = Employee()
        empl.firstname = self.request.get('firstname')
        empl.lastname = self.request.get('lastname')
        empl.email = email
        empl.employer = self.request.get('employer')
        empl.workplace = self.request.get('workplace')
        if hasAccomodationRight(empl.workplace):
            if (self.request.get('accomodation')):
                empl.accomodation = 'yes'
                empl.residence = self.request.get('residence')
                empl.roommate = self.request.get('roommate')
            else:
                empl.accomodation = 'no'
        
        self.saveToSession(empl)
        self.redirect('/movieAnkete')

def addList( list, listToAdd ):
    for i in range( len(list) ):
        list[i] += listToAdd[i]
        
def sendMail(empl):
    userAddress = empl.email
    senderAddress = MAIL_FROM
    subject = MAIL_SUBJECT
    #todo convert database data to displayable
    body = MAIL_TEXT % \
    {
        FIRST_NAME      : empl.firstname,
        LAST_NAME       : empl.lastname,
        EMPLOYER        : eployerLabels[empl.employer],
        WORKPLACE       : workplaces[ empl.workplace ],
        ACCOMODATION    : accomodationLabels[ empl.accomodation ],
        RESIDENCE       : empl.residence,
        ROOMMATE        : empl.roommate,
        CHARACTER       : empl.character,
    }
    mail.send_mail(senderAddress, userAddress, subject, body)
    
class MoviePage(BaseHandler):

    def get(self):
        self.displayPage()
        
    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
            'questions': questions,
        }
        template = JINJA_ENVIRONMENT.get_template('movieAnkete.html')
        self.response.write(template.render(template_values))


    def rateAnswers(self):
        maleAnswer = self.request.get(GENDER)
        if maleAnswer == ANKETE_MAIL:
            male = True
        else:
            male = False
        
        results = [ 0 for ch in characters ]
        for ap in anketePoints:
            answer = self.request.get( ap['question'] )
            if answer:
                addList( results, ap['points'][answer])
                
        logging.info('rated answers: ' + str(results))
        return male, results
        
    def validateData(self):
        errors = []
        errorIds = []
        
        if not self.request.get(GENDER):
            errors.append( ERROR_NOT_ENTERED_GENDER )
            errorIds.append(GENDER)
            
        return (errors, errorIds)

            
    def post(self):
        email = self.session.get(EMAIL)
        if not email or existEmpl( email ):
            logging.error('Email not valid: ' + str(email))
            self.abort(400) # bad request
            
        errors, errorIds = self.validateData() 
        if errors:
            self.displayPage( self.request.params, errors, errorIds )
            return
        
        male, results = self.rateAnswers()
        empl = self.getEmployeeFromSession()
        charId = assignCharacter( calculateCharacter( male, results ), male)
        empl.character = characters[charId]
        persistEmployee( empl )
        try:
            sendMail(empl)
        except (Exception, DeadlineExceededError):
            logging.exception('Failed to send email %s ', email)    
            
        # go to results
        query_params = {'chr': charId}
        self.redirect('/?' + urllib.urlencode(query_params))
        
    def getEmployeeFromSession(self):
        empl = Employee()
        empl.firstname     = self.session.get(FIRST_NAME)
        empl.lastname      = self.session.get(LAST_NAME)
        empl.email         = self.session.get(EMAIL)
        empl.employer      = self.session.get(EMPLOYER)
        empl.workplace     = self.session.get(WORKPLACE)
        empl.accomodation  = self.session.get(ACCOMODATION)
        empl.residence     = self.session.get(RESIDENCE)
        empl.roommate      = self.session.get(ROOMMATE)
        empl.character     = self.session.get(CHARACTER)
        return empl
        
class ResultPage(BaseHandler):
            
    def get(self):
        chr = int( self.request.get('chr'))
        template_values = { 
            'characterId' : chr,
            'characterImgs' : characterImgs,
            'characters': characters,
            'characterTexts': characterTexts,
        }
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
        ('/', IntroPage),
        ('/main', MainPage),
        ('/movieAnkete', MoviePage),
        ('/results', ResultPage),
    ], config = sessionConfig)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()