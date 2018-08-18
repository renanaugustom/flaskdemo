from flask import Blueprint, render_template, flash, redirect, url_for
from productmanager import db, bcrypt
from productmanager.user.models import User
from productmanager.user.forms import UserRegisterForm
from flask_login import current_user

user_api = Blueprint('user_api', __name__, template_folder='templates')

@user_api.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('product_api.home'))

    form = UserRegisterForm()

    if form.validate_on_submit():
        print('aqui')
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(form.email.data, form.name.data, hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Account has been created with successs!', 'success')
        return redirect(url_for('home_api.login'))

    return render_template('register.html', title='Register Account', form = form)