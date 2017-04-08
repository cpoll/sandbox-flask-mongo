#!/usr/bin/env python3

from flask import Flask
from server.routes import FIZZBUZZ_BLUEPRINT

APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello World4!"

APP.register_blueprint(FIZZBUZZ_BLUEPRINT)
