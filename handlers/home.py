from google.appengine.api import users
from google.appengine.ext import ndb

import cgi #Common Gateway Interface support
import jinja2
import urllib
import webapp2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader('views'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

CLINIC_DEFAULT = 'default_clinic'

def clinic_key(clinic_name=CLINIC_DEFAULT):
	return ndb.Key('Clinic', clinic_name)

