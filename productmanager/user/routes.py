from flask import Blueprint, render_template, flash, redirect, url_for
from productmanager.user.forms import UserRegisterForm

user_api = Blueprint('user_api', __name__, template_folder='templates')

@user_api.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()

    if form.validate_on_submit():
        flash('User created with successs!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register Account', form = form)