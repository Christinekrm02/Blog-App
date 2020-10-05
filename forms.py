from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#Use Python classes to represent the forms

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    #User can login with uname or email
   # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
  #remeber field stores cookie of user's id and "remebers" them for each login
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')