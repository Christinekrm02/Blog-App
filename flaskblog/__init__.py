#Environment set-up
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
#Use terminal, activate python, import secrets, call secrets.token_hex(number of bytes to generate) to create a randomized secret key
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '24b5d2d61f2b6eb1f45c9767d52aa55a'
app.config['TESTING'] = False
#SQL database will be a local file for now.
#database connection setup. Assigns sqlite path, base directory and name of application to sqlite database. Note that this app.config is pointing to the instantiated Flask class (our app)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#Create instance of database
db = SQLAlchemy(app)
#pwrd encryption
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes