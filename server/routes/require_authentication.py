from flask import jsonify, request
from server.access_api.authentication import Authentication


def require_authentication(user_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            token = request.headers.get('Session-Token')
            authentication = Authentication()
            session_valid = authentication.verify_session(token)

            if session_valid:
                return function(*args, **kwargs)
            else:
                response = jsonify({'message': 'access denied'})
                response.status_code = 401
                return response


        return wrapper
    return decorator
