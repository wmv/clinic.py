from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions


import webapp2

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.redirect(users.create_login_url('/'))

class LogoutHandler(webapp2.RequestHandler):
	def get(self):
		self.redirect(users.create_logout_url('/'))
