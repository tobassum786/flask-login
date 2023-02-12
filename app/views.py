from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from .models import User
from . import db


views = Blueprint('views', __name__)

@views.route('/')
@login_required
def index():
	return render_template("index.html", username=current_user.username)

@views.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		login = User.query.filter_by(username=username).first()

		if not login or not check_password_hash(login.password, password):
			flash("username and password wrong.")
			return redirect(url_for("views.login"))
		
		login_user(login)
		return redirect(url_for("views.index"))
	return render_template("login.html")


@views.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == "POST":
		username = request.form['username']
		password = generate_password_hash(request.form['password'], method='sha256')
		email = request.form['email']

		user = User.query.filter_by(username=username).first()

		if user:
			flash("Email is already exist? ")
			return redirect(url_for("views.register"))

		register = User(username=username, password=password, email=email)

		db.session.add(register)

		db.session.commit()

		return redirect(url_for("views.login"))

	return render_template('register.html')


@views.route("/logout")
def logout():
	logout_user()
	return render_template("index.html")