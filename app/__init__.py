from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()


def create_app():
	app = Flask(__name__, instance_relative_config=False)
	app.config.from_object("config.DevelopmentConfig")

	db.init_app(app)

	from . import models

	with app.app_context():
		db.create_all()

	login_manager = LoginManager()
	login_manager.login_view = 'views.login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(user_id)

	


	from .views import views as views_blueprint
	app.register_blueprint(views_blueprint)


	return app