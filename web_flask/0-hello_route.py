#!/usr/bin/python3
"""Starts a flask web application listening on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask(__name__)


# Define routes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello HBNB"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
