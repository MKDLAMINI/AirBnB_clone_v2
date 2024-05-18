#!/usr/bin/python3
"""
import a Flask module to start a web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greet_holberton():
    """function returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def ret_hbnb():
    """This function returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def input_text(text):
    """display "C", followed by the value of the text variable"""
    return 'C' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def cold_py(text='is cool'):
     """return "Python" followed by the value of the text"""
     return 'Python' + text.replace('_', ' ' )


@app.route('/number/<int:n>', strict_slashes=False)
def ret_number(n):
    """returns "n is a number" only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """returns a n HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

