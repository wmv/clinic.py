from google.appengine.ext import ndb

class Patient(ndb.Model):
	"""Models a Patient entry"""
	name        = ndb.StringProperty()
	id_no       = ndb.StringProperty()
	gender      = ndb.BooleanProperty()
	record_no   = ndb.StringProperty()
	birth_date  = ndb.DateProperty(indexed=True)
	cell_no     = ndb.StringProperty()
	created     = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)
    mugshot     = ndb.BlobProperty()
    email       = ndb.StringProperty()
    employer    = ndb.StringProperty()
    history     = ndb.PickleProperty()
    enrolled_by = ndb.UserProperty()

class Consultation(ndb.Model):
	"""Models a Consultation entry"""
	patient_key       = ndb.IntegerProperty()
	consultation_type = ndb.IntegerProperty()
	created           = ndb.DateTimeProperty(auto_now_add=True)
	consultation_date = ndb.DateTimeProperty()
	completed         = ndb.BooleanProperty()
	price             = ndb.FloatProperty()
	made_by           = ndb.UserProperty()
	