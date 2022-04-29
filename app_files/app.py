from flask import Flask, render_template
import os
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
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

@app.route('/calc/')
def calc():
    return render_template('calc.html')

@app.route('/calc/<operator>/<int:num1>/<int:num2>/')
def calc_result(operator, num1, num2):
    operator = escape(operator) 
    if operator == "add":
        procedure = f'{num1} + {num2}'
        result = num1 + num2
    
    if operator == "subtract":
        procedure = f'{num1} - {num2}'
        result = num1 - num2
    
    if operator == "multiply":
        procedure = f'{num1} * {num2}'
        result = num1 * num2

    if operator == "divide":
        try:
            result = num1 / num2
            procedure = f'{num1} * {num2}'
        except ZeroDivisionError:
            return "Can't divide by zero. <a href='/calc'>Go back</a>."

    return render_template(
        'calc_result_templ.html',
        procedure = procedure,
        result = result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
