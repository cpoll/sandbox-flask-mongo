#!/usr/bin/env python3
from flask import Flask
from .routes.fizzbuzz.fizzbuzz_route import FIZZBUZZ_BLUEPRINT

APP = Flask(__name__)

@APP.route("/")
def hello():
    return "Hello World4!"

print("hi")

APP.register_blueprint(FIZZBUZZ_BLUEPRINT)
