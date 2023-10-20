#!/usr/bin/python3
"""Starts a flask web application listening on 0.0.0.0, port 5000
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


# Define routes
@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def handle_states(id=None):
    """displays states list"""

    states = storage.all(State).values()
    try:
        state = [state for state in states if state.id == id][0]
    except Exception as e:
        state = None
    
    return render_template("9-states.html", states=states, state=state, id=id)


@app.teardown_appcontext
def close(self):
    """close the session after requests """
    storage.close()

if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
