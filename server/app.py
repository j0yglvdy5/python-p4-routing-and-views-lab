#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:param>')
def print_string(param):
    param = 'hello'
    return param
@app.route('/count/<int:param>')
def count(param):
    numbers = list(range(param + 1))
    return '<br>'.join(map(str,numbers))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'
    return f'{num1}, {operation} ,{num2} = {result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
