from google.appengine.api import users
from google.appengine.ext import ndb
from models import *

import cgi
import jinja2
import urllib
import webapp2
import os
import logging
import datetime

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader('views'),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

CLINIC_DEFAULT = 'default_clinic'

def clinic_key(clinic_name=CLINIC_DEFAULT):
	return ndb.Key('Clinic', clinic_name)

def PatientById(id):
    return Patient.get_by_id(id, parent=clinic_key())

def ConsultationById(id):
    return Consultation.get_by_id(id, parent=clinic_key())

class NewPatientHandler(webapp2.RequestHandler):
	def post(self):
		patient = Patient(parent=clinic_key(CLINIC_DEFAULT))
		
		if users.get_current_user():
			patient.enrolled_by = users.get_current_user()

		patient.name       = self.request.get('p_name')
		patient.id_no      = self.request.get('p_id')
		patient.gender     = self.request.get('p_gender')
		patient.record_no  = self.request.get('p_record_no')
		patient.birth_date = self.request.get('p_id')
		patient.cell_no    = self.request.get('p_cell_no')
	    patient.mugshot    = self.request.get('p_mugshot')
	    patient.email      = self.request.get('p_email')
	    patient.employer   = self.request.get('p_employer')
	    patient.history    = self.request.get('p_history')

	    if patient.enrolled_by:
	    	patient.last_mod = patient.enrolled_by
	    else:
	    	patient.last_mod = users.get_current_user()

	    if patient.created:
	    	patient.last_update = patient.created
	    else:
	    	patient.last_update = datetime.datetime.now()

		patient.put()
		
		self.redirect('/')


class NewConsultationHandler(webapp2.RequestHandler):
	def post(self):
		con = Consultation(parent=clinic_key(CLINIC_DEFAULT))
		
		if users.get_current_user():
			con.made_by   = users.get_current_user()

		con.patient_key       = self.request.get('p_key')
		con.consultation_type = self.request.get('c_type')
		con.consultation_date = self.request.get('c_date')
		con.completed         = self.request.get('c_completed')
		con.price             = self.request.get('c_price')

		con.put()
		
		self.redirect('/')

class DeletePatientHandler(webapp2.RequestHandler):
    def post(self):
        id = int(self.request.get('p_id'))
        patient = PatientById(id)
        patient.key.delete()
        self.redirect('/')

class DeleteConsultationHandler(webapp2.RequestHandler):
    def post(self):
        id = int(self.request.get('c_id'))
        con = ConsultationById(id)
        con.key.delete()
        self.redirect('/')

class EditPatientHandler(webapp2.RequestHandler):
	def get(self, patient_id):
		logging.debug("Inside patient edit get method")
		id = int(patient_id)
		patient = PatientById(id)

		template_values = {
			'p_name':       patient.name
			'p_id_no':      patient.id_no
			'p_gender':     patient.gender
			'p_record_no':  patient.record_no
			'p_birth_date': patient.birth_date
			'p_cell_no':    patient.cell_no
		    'p_mugshot':    patient.mugshot
		    'p_email':      patient.email
		    'p_employer':   patient.employer
		    'p_history':    patient.history
			}

		template = JINJA_ENVIRONMENT.get_template('edit_p.html')
		self.response.write(template.render(template_values))

	def post(self):
		logging.debug("Inside patient edit post method")
		id = int(self.request.get('p_id'))
		patient = PatientById(id)

		patient.name       = self.request.get('p_name')
		patient.id_no      = self.request.get('p_id')
		patient.gender     = self.request.get('p_gender')
		patient.record_no  = self.request.get('p_record_no')
		patient.birth_date = self.request.get('p_id')
		patient.cell_no    = self.request.get('p_cell_no')
	    patient.mugshot    = self.request.get('p_mugshot')
	    patient.email      = self.request.get('p_email')
	    patient.employer   = self.request.get('p_employer')
	    patient.history    = self.request.get('p_history')

		patient.put()

		self.redirect('/')


class EditConsultationHandler(webapp2.RequestHandler):
	def get(self, consultation_id):
		logging.debug("Inside consultation edit get method")
		id = int(consultation_id)
		con = ConsultationById(id)

		template_values = {     
			'c_type':      con.consultation_type           
			'c_date':      con.consultation_date 
			'c_completed': con.completed         
			'c_price':     con.price             
			}

		template = JINJA_ENVIRONMENT.get_template('edit_c.html')
		self.response.write(template.render(template_values))

	def post(self):
		logging.debug("Inside consultation edit post method")
		id = int(self.request.get('c_id'))
		con = ConsultationById(id)

		con.consultation_type = self.request.get('c_type')
		con.consultation_date = self.request.get('c_date')
		con.completed         = self.request.get('c_completed')
		con.price             = self.request.get('c_price')

		con.put()

		self.redirect('/')