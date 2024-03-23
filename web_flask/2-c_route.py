#!/usr/bin/python3
"""web flask application"""
from flask import Flask
app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_route():
    """return string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_route2():
    """return string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_route3(text):
    """return text from html request"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)