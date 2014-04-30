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

from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore, ndb
import urllib



settings.configure()
settings.USE_I18N = False
settings.TEMPLATE_DIRS = ('.')
settings.TEMPLATE_DEBUG = True
    
def render_template(response, template_file, template_values):
    response.out.write( render_to_string(template_file, template_values))
  

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        try:
            logging.info('Posting data: %s', self.request.POST)
            photo_key = self.save_file()
            
            form = Page1Form(data = self.request.params) 
            if not form.is_valid():
                self.displayPage( form=form )
                return
    
            form.save(photo_key)
        except:
            logging.exception('Error when posting data')
        
        self.redirect(URL_PAGE_2)
        
    def save_file(self):
        try:
            upload_files = self.get_uploads('photo')
            logging.info(self.request.POST)
            blob_info = upload_files[0]
            key = blob_info.key()
            logging.info("Blob info: %s", key)
            return key
        except:
            logging.exception('Unable to store file')
            return None
        
         
class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        if not blob_info:
            self.error(404)
            
        self.send_blob(blob_info)


class Page1(BaseHandler):

    def displayPage(self, **kwargs):
        render_template(self.response, 'page1.html', kwargs)
        
    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        self.displayPage(form=Page1Form(), upload_url=upload_url)
        
        
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
        (URL_PHOTO + '/([^/]+)?', ServeHandler),
        ('/upload', UploadHandler)
    ], config = sessionConfig, debug=True)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()