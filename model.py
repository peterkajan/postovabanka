from google.appengine.ext import ndb

    
class Record(ndb.Model):
    activity = ndb.StringProperty(required = True)
    joke = ndb.TextProperty()
    #photo = ndb.StringProperty(required = True)
    
    
    
     
        
# def persistGuest( empl ):
#     #todo another email check 
#     key = ndb.Key(Guest, empl.email)    
#     entity = Guest(key=key)
#     entity.set(empl)
#     entity.put()
