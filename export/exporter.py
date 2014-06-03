# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from google.appengine.ext import ndb

class Record(db.Model):
    my_activity = db.StringProperty()
    joke = db.TextProperty()
    time_filled = db.DateTimeProperty()
    name = db.StringProperty()
    photo_link = db.StringProperty()
    

conv = {
    "=ED": u'í',
    "=E1": u'á',
    "=B9": u'š',
    "=BB": u'ť',
    "=FA": u'ú',
    "=EF": u'ď',
    "=B5": u'ľ',
    "=F2": u'ň',
    "=FD": u'ý',
    "=E8": u'č',
    "=BE": u'ž',
    "=E9": u'é',
    "=AE": u'Ž',
    "=F3": u'ó',
    "=A9": u'Š',
    "=F4": u'ô',
    "=C8": u'Č',
    "=E4": u'ä',
    "=AB": u'Ť',
    "=CD": u'Í',
}

def toUtf8( elem ):
    if (elem):
        for badchar, goodchar in conv.items():
            elem = unicode(elem).replace(badchar, goodchar)
        return elem.encode('utf-8')
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