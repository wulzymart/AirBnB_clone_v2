#!/usr/bin/python3
"""Starts a flask web application listening on 0.0.0.0, port 5000
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template


app = Flask(__name__)


# Define routes
@app.route('/hbnb', strict_slashes=False)
def handle_filters(id=None):
    """displays states list"""

    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    return render_template("100-hbnb.html", states=states, amenities=amenities,
                           places=places)


@app.teardown_appcontext
def close(self):
    """close the session after requests """
    storage.close()


if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
