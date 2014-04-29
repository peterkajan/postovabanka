from defines import *
from django.conf import settings
from forms import Page1Form
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from utils import BaseHandler, sessionConfig
import logging
import webapp2
from django.template.loader import render_to_string
from google.appengine.ext import ndb


settings.configure()
settings.USE_I18N = False
settings.TEMPLATE_DIRS = ('.')
settings.TEMPLATE_DEBUG = True
    
def render_template(response, template_file, template_values):
    response.out.write( render_to_string(template_file, template_values))


class Page1(BaseHandler):

    def displayPage(self, form):
        template_values = {
            'form': form,
        }
        render_template(self.response, 'page1.html', template_values)
        
    def get(self):
        self.displayPage( Page1Form())
                         
    def post(self):
        logging.info('Posting data: %s', self.request.POST)
        form = Page1Form(data = self.request.params) 
        if not form.is_valid():
            self.displayPage( form )
            return

        form.save(self.request.get('photo'))
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
    
class PhotoPage(BaseHandler):
    def get(self):
        key = ndb.Key( urlsafe = self.request.get('key') )
        rec = key.get()
        if rec.photo:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(rec.photo)
        else:
            self.error(404)

application = webapp2.WSGIApplication([
        (URL_PAGE_1, Page1),
        (URL_PAGE_2, Page2),
        (URL_PHOTO, PhotoPage),
    ], config = sessionConfig, debug=True)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()