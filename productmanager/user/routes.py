from flask import Blueprint, render_template, flash, redirect, url_for, request
from productmanager import db, bcrypt
from productmanager.user.models import User
from productmanager.user.forms import UserRegisterForm, UserUpdateForm
from flask_login import current_user

user_api = Blueprint('user_api', __name__, template_folder='templates')

@user_api.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('product_api.home'))

    form = UserRegisterForm()

    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(form.email.data, form.name.data, hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created with successs!', 'success')
        return redirect(url_for('home_api.login'))

    return render_template('register.html', title='Register Account', form = form)

@user_api.route('/update', methods=['GET', 'POST'])
def update():
    form = UserUpdateForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.email.data = current_user.email

    return render_template('update.html', title='Update Account', form = form)