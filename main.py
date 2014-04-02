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
    
URL_PAGE_1='/'
URL_PAGE_2='/informacie'
URL_PAGE_3='/potvrdenie'

#move to utils
def isEmailValid( email ):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class Page1(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        template = JINJA_ENVIRONMENT.get_template('page1.html')
        self.response.write(template.render(template_values))
        
    def get(self):
        self.displayPage()
                         
    def validateData(self):
        errors = []
        errorIds = []
        
        return errors, errorIds
            
            
    def post(self):
        errors, errorIds = self.validateData() 
        if errors:
            self.displayPage( self.request.params, errors, errorIds )
            return

        self.redirect(URL_PAGE_2)
        
        
class Page2(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        template = JINJA_ENVIRONMENT.get_template('page2.html')
        self.response.write(template.render(template_values))
        
    def get(self):
        self.displayPage()
                         
    def validateData(self):
        errors = []
        errorIds = []
        
        return errors, errorIds
            
            
    def post(self):
        errors, errorIds = self.validateData() 
        if errors:
            self.displayPage( self.request.params, errors, errorIds )
            return

        self.redirect(URL_PAGE_3)
        
        
class Page3(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        template = JINJA_ENVIRONMENT.get_template('page3.html')
        self.response.write(template.render(template_values))
        
    def get(self):
        self.displayPage()
                         
        
# def sendMail(empl):
#     userAddress = empl.email
#     senderAddress = MAIL_FROM
#     subject = MAIL_SUBJECT
#     #todo convert database data to displayable
#     body = MAIL_TEXT % \
#     {
#         FIRST_NAME      : empl.firstname,
#         LAST_NAME       : empl.lastname,
#         EMPLOYER        : eployerLabels[empl.employer],
#         WORKPLACE       : workplaces[ empl.workplace ],
#         ACCOMODATION    : accomodationLabels[ empl.accomodation ],
#         RESIDENCE       : empl.residence,
#         ROOMMATE        : empl.roommate,
#         CHARACTER       : empl.character,
#     }
#     mail.send_mail(senderAddress, userAddress, subject, body)
    

application = webapp2.WSGIApplication([
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
        (URL_PAGE_3, Page3),
    ], config = sessionConfig)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()