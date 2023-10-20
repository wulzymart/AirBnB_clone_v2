#!/usr/bin/python3
"""Starts a flask web application listening on 0.0.0.0, port 5000
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


# Define routes
@app.route('/states_list', strict_slashes=False)
def handle_states_list():
    """displays states list"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close(self):
    """close the session after requests """
    storage.close()


if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
