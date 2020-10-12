from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.models import User,Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user .is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #Generate protected password from the data passed into the password field. Do this in strings instead of bytes
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #create new instance of user for each registration. Do now pass in the original password they registered with, instead use the hased version
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #To run the server in test mode, call import the db from flaskblog and then run db.create_all()
        flash('Account created! Go ahead and login to get started!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if current_user .is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account',  methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated', 'success')
        #pay attention to post, get redirect to avoid 'are you sure you want to reload?" message
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data =  current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)
