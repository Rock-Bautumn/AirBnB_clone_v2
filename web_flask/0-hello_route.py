#!/usr/bin/python3
"""
Make a web server with a basic hello world
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    Basic hello world
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    """ Start the app """
    app.run(host="0.0.0.0", port=5000)
