from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Test'}
    posts = [ # mocked posts data
        {
            'author': {'nickname': 'Wally'},
            'body': 'Great article!'
        },
        {
            'author': {'nickname': 'Brenda'},
            'body': 'Interesting article!'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title='Sign In',
                            form=form)
