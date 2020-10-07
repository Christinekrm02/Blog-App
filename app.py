#Environment set-up
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)
#Use terminal, activate python, import secrets, call secrets.token_hex(number of bytes to generate) to create a randomized secret key
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '24b5d2d61f2b6eb1f45c9767d52aa55a'
#SQL database will be a local file for now.
#database connection setup. Assigns sqlite path, base directory and name of application to sqlite database. Note that this app.config is pointing to the instantiated Flask class (our app)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
#Create instance of database
db = SQLAlchemy(app)

#Create users (as classes)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    #1:many == user:posts
    posts = db.relationship('Post', backref='author', lazy=True)
    #Output when a user obj is printer
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title= db.Column(db.String(100), nullable=False)
     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     def __repr__(self):
         return f"Post('{self.title}', '{self.date_posted}')"



posts = [
    {
        'author': 'Chrissy Em',
        'title': 'Blog Post 2',
        'content': 'Some content',
        'date_posted': 'July 1, 2020'
    },
    {
        'author': 'Chris Em',
        'title': 'Blog Post 1',
        'content': 'Some content 1',
        'date_posted': 'July 10, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', name='Christine')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',  methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       if form.email.data == 'admin@blog.com' and form.password.data == 'password':
           flash('You have been logged in!', 'success')
           return redirect(url_for('home'))
       else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

  

