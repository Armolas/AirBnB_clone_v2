#!/usr/bin/python3
"""This module starts a web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
import os

app = Flask(__name__)
states = storage.all(State)
storageType = os.getenv('HBNB_TYPE_STORAGE')
db = False
if storageType == 'db':
    db = True


@app.teardown_appcontext
def close(exception=None):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns an html list of all states"""
    return render_template("7-states_list.html", states=states)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """returns an html list of cities sorted by states"""
    return render_template("8-cities_by_states.html", states=states, db=db)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
