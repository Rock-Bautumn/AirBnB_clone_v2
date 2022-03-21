#!/usr/bin/python3
"""
Make a web app with some basic routes
"""
from flask import Flask

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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun_but_python_not_so_much_route(text):
    """
    Using a variable in the route name
    """
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    """ Start the app """
    app.run(host="0.0.0.0", port=5000)
