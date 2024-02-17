#!/usr/bin/python3

from flask import Flask
from markupsafe import escape


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB' at the root dorectory"""
    return 'Hello HBNB!'

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays "HBNB" at root /hbnb"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """displays C followed by the text inputed"""
    return f"C {escape(text.replace('_', ' '))}"

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
def py_route(text, default='is cool'):
    """displays python followed by the text or is cool"""
    return f"Python {escape(text.replace('_', ' '))}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
