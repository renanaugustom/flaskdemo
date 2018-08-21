from flask import Blueprint, render_template, flash, redirect, url_for, request
from productmanager import db, bcrypt
from productmanager.forms import LoginForm
from productmanager.user.models import User
from flask_login import login_user, current_user, logout_user, login_required

home_api = Blueprint('home_api', __name__, template_folder='templates')

@home_api.route("/")
@login_required
def hello():
    return "Hello World!"

@home_api.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('product_api.home'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('product_api.home'))
        else:
            flash('Login Unsucessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form = form)

@home_api.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home_api.login'))