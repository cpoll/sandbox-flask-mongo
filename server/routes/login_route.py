import json
from flask import Blueprint, jsonify, request
from server.access_api.authentication import Authentication


LOGIN_BLUEPRINT = Blueprint('login', __name__)


@LOGIN_BLUEPRINT.route('/login/', methods=["POST"])
def login_route():

    username = request.args.get('login')
    password = request.data.decode('utf-8') # TODO: Make sure utf-8 works in all cases

    authentication = Authentication()
    auth_token = authentication.authenticate(username, password)

    if auth_token:
        return auth_token
    else:
        response = jsonify({'message': 'login failed'})
        response.status_code = 401
        return response
