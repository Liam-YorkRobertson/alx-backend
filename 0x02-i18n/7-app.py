#!/usr/bin/env python3
"""
basic flask application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    get user dictionary
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """
    executed before other functions
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    get best match with supported languages
    """
    current_locale = request.args.get('locale')
    user_locale = g.user.get('loc'
                             'ale') if g.user and 'locale' in g.user else None
    header_locale = request.headers.get('Accept'
                                        '-Language', '').split(',')[0].strip()
    for locale in (current_locale, user_locale,
                   header_locale, app.config['BABEL_DEFAULT_LOCALE']):
        if locale and locale in app.config['LANGUAGES']:
            return locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone() -> str:
    """
    get user's preferred timezone
    """
    timezones = (
        request.args.get('timezone'),
        g.user.get('timezone') if g.user and 'timezone' in g.user else None,
        app.config['BABEL_DEFAULT_TIMEZONE']
    )
    for timezone in timezones:
        if timezone and pytz.timezone(timezone, None):
            return timezone

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    route for the index page
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
