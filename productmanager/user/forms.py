from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from productmanager.user.models import User

class UserRegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(max=120)])    
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('E-mail is already registered.')

class UserUpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(max=120)])

    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('E-mail is already registered.')