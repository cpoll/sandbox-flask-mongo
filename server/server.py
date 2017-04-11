#!/usr/bin/env python3
from flask import Flask

from .routes.fizzbuzz_route import FIZZBUZZ_BLUEPRINT
from .routes.login_route import LOGIN_BLUEPRINT

APP = Flask(__name__)


@APP.route("/")
def hello():
    return "Hello World4!"

APP.register_blueprint(FIZZBUZZ_BLUEPRINT)
APP.register_blueprint(LOGIN_BLUEPRINT)
