#!/usr/bin/python3
"""
import a Flask module to start a web application
"""

from flask import Flask
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

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='5000')
