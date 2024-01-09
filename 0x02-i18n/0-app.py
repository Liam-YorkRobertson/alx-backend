#!/usr/bin/env python3
"""
basic flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def basic():
    """
    route for the index page
    """
    return render_template('0-index.html',
                           title="Welcome to Holberton",
                           header="Hello world")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
