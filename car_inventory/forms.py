from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class CarForm(FlaskForm):
    make = StringField('make')
    model = StringField('model')
    price = DecimalField('price', places = 2)
    mpg = StringField('mpg')
    max_speed = IntegerField('max_speed')
    submit_button = SubmitField()
