#!/usr/bin/env python3
"""
basic flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    config for lang and time
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale():
    """
    get best match with supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    route for the index page
    """
    return render_template('2-index.html',)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
