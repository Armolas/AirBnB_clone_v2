#!/usr/bin/python3
"""This module starts a web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)
states = storage.all(State)


@app.teardown_appcontext
def close(exception=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns an html list of all states"""
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
