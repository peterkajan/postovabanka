from google.appengine.ext import ndb

    
class Record(ndb.Model):
    joke = ndb.TextProperty()
    time_filled = ndb.DateTimeProperty(auto_now=True)
    #photo = ndb.StringProperty(required = True)
    
    
def update_counter(counterCls, activity_id, label):
    ctr = counterCls.get_or_insert( str(activity_id))
    ctr.cnt += 1
    ctr.id = activity_id
    ctr.label = label
    ctr.put()
        
class Counter(ndb.Model):
    cnt = ndb.IntegerProperty(default=0)
    id = ndb.IntegerProperty()
    label = ndb.StringProperty()
    
        
class Activity(Counter):
    pass

class ActivityType(Counter):
    pass

class ActivitySport(Counter):
    pass
        
     
        
# def persistGuest( empl ):
#     #todo another email check 
#     key = ndb.Key(Guest, empl.email)    
#     entity = Guest(key=key)
#     entity.set(empl)
#     entity.put()
