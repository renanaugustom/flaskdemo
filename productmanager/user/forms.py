from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserRegisterForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Length(min=3, max=40)])    
    password = StringField('Password')