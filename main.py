import defines
from django.conf import settings
from forms import Page1Form
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from utils import BaseHandler, sessionConfig
import logging
import os
import webapp2
from model import persistTestGuests, Guest
from google.appengine.ext import ndb
from google.appengine.runtime import DeadlineExceededError


settings.configure()
settings.USE_I18N = False

    
URL_PAGE_1='/'
URL_PAGE_2='/informacie'
URL_PAGE_3='/potvrdenie'
URL_PAGE_REJECT='/neucast'

URL_PAGE_SENDER='/send_mails_secret'
URL_PAGE_TEST_DATA_IMPORT='/import_secret'

if defines.PAGE_FLOW_2:
    URL_PAGE_2 = URL_PAGE_3


def render_template(response, template_file, template_values):
    path = os.path.join(os.path.dirname(__file__), template_file)
    response.out.write(template.render(path, template_values))
    

def _getKey(handler):
    key = None
    keyUrl = handler.request.get('key')
    if not keyUrl:
        keyUrl = handler.session.get('key')
        
    if keyUrl:
        try:
            key = ndb.Key( urlsafe = keyUrl )
            handler.session['key'] = key.urlsafe()
        except (BaseException):
            logging.exception('Failed to create key: %s', keyUrl)    
    else:
        logging.info('No key in url or session')
    
    return key

def _getGuest(handler, key):
    guest = None
    try:
        guest = key.get()
        if not guest:
            logging.error('Guest is None, key: %s', key.urlsafe())
        
    except (BaseException):
        logging.exception('Failed to get guest, key: %s', key.urlsafe())
        
    return guest
    
class Page1(BaseHandler):

    def displayPage(self, **kwargs):
        render_template(self.response, 'page1.html', kwargs)
        
    def displayAnonymPage(self, **kwargs):
        render_template(self.response, 'page1_anonym.html', kwargs)
        
    def get(self):
        key = _getKey(self)
        if not key:
            return self.displayAnonymPage()
        
        guest = _getGuest(self, key)
        if not guest:
            return self.displayAnonymPage()
        
        logging.info('GET guest: ' + unicode(guest.firstname) 
            + ' ' + unicode(guest.lastname  + ' ' + guest.email))   
        
        return self.displayPage( firstname=guest.firstname )  
                         
    def validateData(self):
        errors = []
        errorIds = []
        return errors, errorIds
            
    def post(self):
        key = ndb.Key( urlsafe = self.session.get('key'))
        guest = _getGuest(self, key)
        if 'accept' in self.request.POST:
            guest.attend = 1
            guest.put()
            sendConfirmationMail(guest)
            return self.redirect(URL_PAGE_2)
        else:
            guest.attend = 0
            guest.put()
            if defines.MAIL_REJECTION:
                sendRejectionMail(guest, generateLink(guest))
            return self.redirect(URL_PAGE_REJECT)
        
        
class Page2(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        render_template(self.response, 'page2.html', template_values)
        
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

    def displayPage(self, **kwargs):
        render_template(self.response, 'page3.html', kwargs)
  
    def get(self):
        key = ndb.Key( urlsafe = self.session.get('key'))
        guest = _getGuest(self, key)
        self.displayPage(firstname=guest.firstname)
        
class PageReject(BaseHandler):

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        render_template(self.response, 'pageReject.html', template_values)
  
    def get(self):
        self.displayPage()
                         

class SenderPage(BaseHandler):
    def get(self):
        out = '\n'
        links = []
        for guest in Guest.query().fetch():
            link = generateLink(guest)
            out += unicode( guest.firstname ) + ' ' + unicode( guest.lastname ) + '\n' + \
                    ' ' + link + '\n';
            #sendInvitationMail(guest, link)
            links.append(link)       
            
        logging.info('Links:\n' + out);
        logging.info('Links machine:\n%s', links);
        self.abort(404)                  
        
def generateLink(guest):
    return defines.DOMAIN + '?key=' + guest.key.urlsafe()

def _sendMail(senderAddress, userAddress, subject, body):
    try:
        mail.send_mail(senderAddress, userAddress, subject, body)
    except (Exception, DeadlineExceededError):
        logging.exception('Failed to send email %s ', userAddress) 
            
def sendInvitationMail(guest, link):
    logging.info('Sending invitation mail sent to %s', guest.email)
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_INVITATION_SUBJECT
    body = defines.MAIL_INVITATION_TEXT.format(name=guest.firstname, link=link)
    _sendMail(senderAddress, userAddress, subject, body)
    logging.info('Invitation mail sent successfully')
    
def sendConfirmationMail(guest):
    logging.info('Sending confirmation mail to %s', guest.email)
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_CONFIRMATION_SUBJECT
    body = defines.MAIL_CONFIRMATION_TEXT.format(name=guest.firstname,)
    _sendMail(senderAddress, userAddress, subject, body)
    logging.info('Confirmation mail sent successfully')
    
def sendRejectionMail(guest, link):
    logging.info('Sending rejection mail to %s', guest.email)
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_REJECTION_SUBJECT
    body = defines.MAIL_REJECTION_TEXT.format(name=guest.firstname, link=link)
    _sendMail(senderAddress, userAddress, subject, body)
    logging.info('Rejection mail sent successfully')
    
class TestDataImportPage(BaseHandler):
    def get(self):
        persistTestGuests()
        self.abort(404)
    


if defines.PAGE_FLOW_2:
    flow_pages = [
        (URL_PAGE_1, Page1),
        (URL_PAGE_3, Page3),
    ]
else:
    flow_pages = [    
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
        (URL_PAGE_3, Page3),
    ]        
    
pages = flow_pages + [
    (URL_PAGE_REJECT, PageReject),
    (URL_PAGE_SENDER, SenderPage),
    (URL_PAGE_TEST_DATA_IMPORT, TestDataImportPage)]
    
application = webapp2.WSGIApplication(pages, config = sessionConfig)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()