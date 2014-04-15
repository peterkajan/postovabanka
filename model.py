from google.appengine.ext import ndb

def exist(key):
    return key.get()

def existGuest( email ):
    key = ndb.Key(Guest, email)
    return exist(key)

    
class Guest(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    email = ndb.StringProperty()
    custom1 = ndb.StringProperty()
    custom2 = ndb.StringProperty()
    note = ndb.StringProperty()
 
        
def persistGuest( empl ):
    #todo another email check 
    key = ndb.Key(Guest, empl.email)    
    entity = Guest(key=key)
    entity.set(empl)
    entity.put()
