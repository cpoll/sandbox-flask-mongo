import json
from flask import Blueprint, jsonify
from server.helpers.fizzbuzz_helper import get_fizzbuzz_range
from server.access_api.fizzbuzzcache import FizzbuzzCache


FIZZBUZZ_BLUEPRINT = Blueprint('fizzbuzz', __name__)


@FIZZBUZZ_BLUEPRINT.route('/fizzbuzz/<number>', methods=["GET"])
def fizzbuzz_route(number):
    try:
        number = int(number)
    except ValueError:
        response = jsonify({'message': 'input must take the form of /fizzbuzz/<number>'})
        response.status_code = 400
        return response

    fizzbuzz_cache = FizzbuzzCache()
    fizzbuzz_value = fizzbuzz_cache.get_fizzbuzz_value(number)

    if not fizzbuzz_value:
        print("fizzbuzz cache miss")
        fizzbuzz_value = get_fizzbuzz_range(number)
        fizzbuzz_cache.cache_fizzbuzz_value(number, fizzbuzz_value)

    return json.dumps({'fizzbuzz': fizzbuzz_value})
