# -*- coding: utf-8 -*-
from google.appengine.ext import ndb

def exist(key):
    return key.get()

    
class Guest(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    email = ndb.StringProperty()
    custom1 = ndb.StringProperty()
    custom2 = ndb.StringProperty()
    note = ndb.StringProperty()
    attend = ndb.IntegerProperty(default=0)


def persistTestGuests():
    for i in range(10):
        g = Guest()
        g.firstname = 'Jožko{}'.format(i)
        g.lastname = 'Mrkvička{}'.format(i)
        g.email = 'jozko{}@geustflow.sk'.format(i)
        g.put()