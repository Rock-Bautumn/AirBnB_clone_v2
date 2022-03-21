#!/usr/bin/python3
"""
Make a web app with some basic routes
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    basic hello world
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    hello world for hbnb route
    """
    return "HBNB"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ show the post with the given id, the id is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ show an html page using a template"""
    return render_template('5-number.html', n=n)


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun_but_python_not_so_much_route(text):
    """
    Using a variable in the route name
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
# @app.route("/python/")
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    return f"Python {text.replace('_', ' ')}"

if __name__ == '__main__':
    """ Start the app """
    app.run(host="0.0.0.0", port=5000)
