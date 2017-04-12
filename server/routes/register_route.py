from flask import Blueprint, jsonify, request
from server.access_api.accounts import Accounts


REGISTER_BLUEPRINT = Blueprint('register', __name__)


@REGISTER_BLUEPRINT.route('/register/', methods=["POST"])
def login_route():

    username = request.args.get('login')
    password = request.data.decode('utf-8') # TODO: Make sure utf-8 works in all cases

    accounts = Accounts()
    result = accounts.create_user(username, password)

    if result:
        return '', 200
    else:
        response = jsonify({'message': 'account creation failed'})
        response.status_code = 409
        return response
