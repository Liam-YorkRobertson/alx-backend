#!/usr/bin/env python3
"""
basic flask application
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config for lang and time
    """
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = "en"
    DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def basic():
    """
    route for the index page
    """
    return render_template('1-index.html',
                           title="Welcome to Holberton",
                           header="Hello world")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
