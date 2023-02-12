from os import environ, path
from dotenv import load_dotenv
import os


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config():
	FLASK_DEBUG = 'True'
	TESTING = 'True'

	
	SECRET_KEY = environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.sqlite3'
	SQLALCHEMY_TRACK_MODIFICATIONS ='False'


	
class DevelopmentConfig(Config):
	FLASK_DEBUG = 'True'
	TESTING = 'True'
	SECRET_KEY = environ.get("SECRET_KEY")

	SQLALCHEMY_DATABASE_URI = 'sqlite:///app.sqlite3'
	SQLALCHEMY_TRACK_MODIFICATIONS ='False'


class ProductionConfig(Config):
	FLASK_DEBUG = 'False'


