#!/usr/bin/env python3

from server import APP
from server.routes.fizzbuzz.fizzbuzz_route import FIZZBUZZ_BLUEPRINT

@APP.route("/")
def hello():
    return "Hello World4!"

APP.register_blueprint(FIZZBUZZ_BLUEPRINT)
