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


settings.configure()
settings.USE_I18N = False

    
URL_PAGE_1='/'
URL_PAGE_2='/informacie'
URL_PAGE_3='/potvrdenie'
URL_PAGE_REJECT='/nezucatnim'

URL_PAGE_SENDER='/send_mails_secret'

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
        except (BaseException):
            logging.exception('Failed to create key: %s', keyUrl)
            handler.abort(404)    
    else:
        logging.info('No key in url or session')
        handler.abort(404)
    
    handler.session['key'] = key.urlsafe()
    return key

def _getGuest(handler):
    key = _getKey(handler);
    try:
        guest = key.get()
        if not guest:
            logging.error('Employee is None, key: %s', key.urlsafe())
            handler.abort(404)
        return guest
    except (BaseException):
        logging.exception('Failed to get guest, key: %s', key.urlsafe())
        handler.abort(404)
    
class Page1(BaseHandler):

    def displayPage(self, **kwargs):
        render_template(self.response, 'page1.html', kwargs)
        
    def get(self):
        guest = _getGuest(self)
        
        logging.info('GET guest: ' + unicode(guest.firstname) 
            + ' ' + unicode(guest.lastname  + ' ' + guest.email))   
        
        self.displayPage( firstname=guest.firstname )  
        
                         
    def validateData(self):
        errors = []
        errorIds = []
        
        return errors, errorIds
            
            
    def post(self):
        guest = _getGuest(self)
        if 'accept' in self.request.POST:
            guest.attend = 1
            guest.put()
            sendConfirmationMail(guest)
            return self.redirect(URL_PAGE_2)
        else:
            guest.attend = 0
            guest.put()
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
        guest = _getGuest(self)
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
        for guest in Guest.query().fetch():
            link = generateLink(guest)
            out += unicode( guest.firstname ) + ' ' + unicode( guest.lastname ) + '\n' + \
                    ' ' + link + '\n';
            sendInvitationMail(guest, link)       
            
        logging.info('Links:\n' + out);
        self.abort(404)                  
        
def generateLink(guest):
    return defines.DOMAIN + '?key=' + guest.key.urlsafe()


def sendInvitationMail(guest, link):
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_INVITATION_SUBJECT
    body = defines.MAIL_INVITATION_TEXT.format(mail_from=defines.MAIL_FROM, link=link)
    mail.send_mail(senderAddress, userAddress, subject, body)
    logging.info('Invitation mail sent to %s', guest.email)
    
def sendConfirmationMail(guest):
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_CONFIRMATION_SUBJECT
    body = defines.MAIL_CONFIRMATION_TEXT.format(mail_from=defines.MAIL_FROM)
    mail.send_mail(senderAddress, userAddress, subject, body)
    logging.info('Confirmation mail sent to %s', guest.email)
    
    
if defines.PAGE_FLOW_2:
    pages = [
        (URL_PAGE_1, Page1),
        (URL_PAGE_3, Page3),
        (URL_PAGE_REJECT, PageReject),
        (URL_PAGE_SENDER, SenderPage)]
else:    
    pages = [
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
        (URL_PAGE_3, Page3),
        (URL_PAGE_REJECT, PageReject),
        (URL_PAGE_SENDER, SenderPage)]
    
application = webapp2.WSGIApplication(pages, config = sessionConfig, debug=True)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()