#Environment set-up
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
#Use terminal, activate python, import secrets, call secrets.token_hex(number of bytes to generate) to create a randomized secret key
app.config['SECRET_KEY'] = '24b5d2d61f2b6eb1f45c9767d52aa55a'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)