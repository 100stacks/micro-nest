from flask import render_template
from app import app

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
