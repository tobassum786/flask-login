from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(256), unique=True)
	email = db.Column(db.String(100), unique=True)

	def is_active(self):
		return True

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

	def generate_password(self, password):
		return generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)