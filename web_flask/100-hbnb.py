#!/usr/bin/python3
"""This module starts a web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User
import os

app = Flask(__name__)
states = storage.all(State)
amen = storage.all(Amenity)
places = storage.all(Place)
users = storage.all(User)
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


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """returns all cities of a state"""
    return render_template(
            "9-states.html", states=states,
            id=f"State.{id}", db=db)


@app.route('/states', endpoint='/states_list', strict_slashes=False)
def states_list():
    """returns an html list of all states"""
    return render_template("7-states_list.html", states=states)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """displays the hbnb filter page"""
    return render_template("10-hbnb_filters.html", states=states, amenities=amen)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays the hbnb filter page"""
    return render_template("100-hbnb.html", states=states, amenities=amen, places=places, users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
