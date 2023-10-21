#!/usr/bin/python3
"""Starts a flask web application listening on 0.0.0.0, port 5000
"""


from flask import Flask, render_template

app = Flask(__name__)


# Define routes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def handle_c(text):
    """handles c route"""
    text = "C " + text.replace('_', ' ')
    return text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def handle_python(text="is cool"):
    """handles the python route"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def handle_num(n):
    """handles the n route"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def handle_num_template(n):
    """handles the number_template route"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def handle_number_odd_or_even(n):
    """handles the number_odd_or_even route"""
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    # Run the application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
