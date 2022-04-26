from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet/')
def hello():
    return render_template('hello.html')

@app.route('/greet/<username>/')
def greet(username):
    return render_template(
        'greet_templ.html',
        username = escape(username))
