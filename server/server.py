#!/usr/bin/env python3

from flask import Flask
from server.routes.fizzbuzz.fizzbuzz_route import FIZZBUZZ_BLUEPRINT

APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello World3!"

APP.register_blueprint(FIZZBUZZ_BLUEPRINT)
