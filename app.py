#Environment set-up
from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)