from defines import *
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
URL_PAGE_2='/potvrdenie'


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
#         errors, errorIds = self.validateData()
        form = Page1Form(data = self.request.params) 
        if not form.is_valid():
            self.displayPage( form )
            return

        self.redirect(URL_PAGE_2)
        
        
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
    

application = webapp2.WSGIApplication([
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
    ], config = sessionConfig)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()