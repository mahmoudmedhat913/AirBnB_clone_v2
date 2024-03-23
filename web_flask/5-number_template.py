#!/usr/bin/python3
"""web flask application"""
from flask import Flask, render_template
app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/')
def hello_route1():
    """return string"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_route2():
    """return string"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_route3(text):
    """return text from html request"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route4(text):
    """return text from html request"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def hello_route5(n):
    """return text from html request formatted as a number"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def hello_route6(n):
    """return text from html template containing a number"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
