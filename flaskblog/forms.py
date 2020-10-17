from flask_wtf import FlaskForm
#Allows user to update user info/picture
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
#Use Python classes to represent the forms

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
   email = StringField('Email', validators=[DataRequired(), Email()])
   password= PasswordField('Password', validators=[DataRequired()])
   confirm_password= PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
   submit = SubmitField('Sign Up')
#Do not alter this syntax. FlaskForm checks for the validate keyword
   def validate_username(self, username):
     user = User.query.filter_by(username=username.data).first()
     if user:
       raise ValidationError('Looks like someone got to it first! That username already exists.')
   def validate_email(self, email):
     user = User.query.filter_by(email=email.data).first()
     if user:
       raise ValidationError('Email is already taken.')
     
class LoginForm(FlaskForm):
    #User can login with uname or email
   # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
  #remeber field stores cookie of user's id and "remebers" them for each login
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#To update username and email address
class UpdateAccountForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
   email = StringField('Email', validators=[DataRequired(), Email()])
   picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
   submit = SubmitField('Update')
#Do not alter this syntax.
   def validate_username(self, username):
     #'If username that user supplies is not the same as a current record of that username...'
     if username.data != current_user.username:
       user = User.query.filter_by(username=username.data).first()
       if user:
         raise ValidationError('Looks like someone got to it first! That username already exists.')
   def validate_email(self, email):
     if email.data != current_user.email:
       user = User.query.filter_by(email=email.data).first()
       if user:
         raise ValidationError('Email is already taken.')
                        
     