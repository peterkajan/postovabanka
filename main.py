from defines import *
from django.conf import settings
from forms import Page1Form
from google.appengine.api import mail
from google.appengine.ext.webapp import template
from utils import BaseHandler, sessionConfig
import logging
import os
import webapp2
from django.template.loader import render_to_string
import urllib
from google.appengine.ext import ndb


settings.configure()
settings.USE_I18N = False
settings.TEMPLATE_DIRS = ('.')
settings.TEMPLATE_DEBUG = True
    
URL_PAGE_1='/'
URL_PAGE_2='/potvrdenie'


def render_template(response, template_file, template_values):
    response.out.write( render_to_string(template_file, template_values))
    
# from google.appengine.ext.webapp import blobstore_handlers
# from google.appengine.ext import blobstore, ndb


# class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
#     def post(self):
#         logging.info(self.request.POST)
#         
#         upload_files = self.get_uploads('photo')  # 'file' is file upload field in the form
#         logging.info(self.request.POST)
#         blob_info = upload_files[0]
#         #self.redirect('/serve/%s' % blob_info.key())
# #         form = Page1Form(data = self.request.params) 
# #         form.save()
# #         self.redirect(URL_PAGE_2)
#         self.redirect('/serve/%s' % blob_info.key())
#         
# class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
#     def get(self, resource):
#         resource = str(urllib.unquote(resource))
#         blob_info = blobstore.BlobInfo.get(resource)
#         self.send_blob(blob_info)


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
        ('/photo', PhotoPage),
    ], config = sessionConfig, debug=True)

def main():
    # Set the logging level in the main function
    # See the section on Requests and App Caching for information on how
    # App Engine reuses your request handlers when you specify a main function
    logging.getLogger().setLevel(logging.INFO)
    

if __name__ == '__main__':
    main()