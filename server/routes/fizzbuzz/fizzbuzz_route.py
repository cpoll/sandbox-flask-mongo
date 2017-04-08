from flask import Blueprint

FIZZBUZZ_BLUEPRINT = Blueprint('fizzbuzz', __name__)
@FIZZBUZZ_BLUEPRINT.route('/fizzbuzz/<number>')
def fizzbuzz_route(number):
    return number
