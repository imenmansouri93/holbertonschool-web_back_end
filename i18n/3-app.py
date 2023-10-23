#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup """
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
""" instantiate the Babel object """


class Config:
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" Use that class as config for Flask app """


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def root():
    """ basic Flask app """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
