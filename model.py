from google.appengine.ext import ndb

    
class Record(ndb.Model):
    my_activity = ndb.StringProperty()
    joke = ndb.TextProperty()
    time_filled = ndb.DateTimeProperty(auto_now=True)
    photo = ndb.BlobProperty()
    name = ndb.StringProperty()
    photo_link = ndb.StringProperty()
    photo_blob_key = ndb.BlobKeyProperty()

    
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

