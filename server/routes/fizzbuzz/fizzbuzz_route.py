import json
from flask import Blueprint, jsonify
from server.helpers.fizzbuzz_helper import get_fizzbuzz_range

FIZZBUZZ_BLUEPRINT = Blueprint('fizzbuzz', __name__)
@FIZZBUZZ_BLUEPRINT.route('/fizzbuzz/<number>')
def fizzbuzz_route(number):
    try:
        number = int(number)
    except ValueError:
        response = jsonify({'message': 'input must take the form of /fizzbuzz/<number>'})
        response.status_code = 400
        return response

    return json.dumps({'fizzbuzz': get_fizzbuzz_range(number)})
