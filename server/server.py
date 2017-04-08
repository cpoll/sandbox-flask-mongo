from flask import Flask

APP = Flask(__name__)
APP.debug = True

@APP.route("/")
def hello():
    return "Hello World!"
