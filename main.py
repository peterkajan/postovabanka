import defines
from django.conf import settings
from forms import Page1Form
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from utils import BaseHandler, sessionConfig
import logging
import os
import webapp2


settings.configure()
settings.USE_I18N = False

    
URL_PAGE_1='/'
URL_PAGE_2='/informacie'
URL_PAGE_3='/potvrdenie'
URL_PAGE_REJECT='/nezucatnim'

if defines.PAGE_FLOW_2:
    URL_PAGE_2 = URL_PAGE_3


def render_template(response, template_file, template_values):
    path = os.path.join(os.path.dirname(__file__), template_file)
    response.out.write(template.render(path, template_values))
    
class Page1(BaseHandler):

    def displayPage(self, form):
        template_values = {
            'form': form,
        }
        render_template(self.response, 'page1.html', template_values)
        
    def get(self):
        self.displayPage( Page1Form())
                         
    def validateData(self):
        errors = []
        errorIds = []
        
        return errors, errorIds
            
            
    def post(self):
        if 'accept' in self.request.POST:
            return self.redirect(URL_PAGE_2)
        else:
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

    def displayPage(self, params={}, errors=[], errorIds=[]):
        template_values = {
            'p': params,
            'errors': errors,
            'errorIds': errorIds,
        }
        render_template(self.response, 'page3.html', template_values)
  
    def get(self):
        self.displayPage()
        
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
                         
                         
        
def sendMail(guest):
    userAddress = guest.email
    senderAddress = defines.MAIL_FROM
    subject = defines.MAIL_SUBJECT
    
    body = defines.MAIL_TEXT
    
    mail.send_mail(senderAddress, userAddress, subject, body)
    
if defines.PAGE_FLOW_2:
    pages = [
        (URL_PAGE_1, Page1),
        (URL_PAGE_3, Page3),
        (URL_PAGE_REJECT, PageReject)]
else:    
    pages = [
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
        (URL_PAGE_3, Page3)]
    
application = webapp2.WSGIApplication(pages, config = sessionConfig, debug=True)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()