from google.appengine.ext import db
from google.appengine.tools import bulkloader
from google.appengine.ext import ndb

class Record(db.Model):
    my_activity = db.StringProperty()
    joke = db.TextProperty()
    time_filled = db.DateTimeProperty()
    name = db.StringProperty()
    photo_link = db.StringProperty()
    

def toUtf8( elem ):
    if (elem):
        return str(elem).encode('utf-8')
    else:
        return None
    
class AlbumExporter(bulkloader.Exporter):
    def __init__(self):
        bulkloader.Exporter.__init__(self, 'Record',
                                    [('my_activity', toUtf8, ''),
                                     ('joke', toUtf8, ''),
                                     ('time_filled', toUtf8, ''),
                                     ('name', toUtf8, ''),
                                     ('photo_link', toUtf8, ''),
                                    ])


exporters = [AlbumExporter]