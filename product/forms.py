from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class ProductRegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=40)])    
    description = StringField('Description')