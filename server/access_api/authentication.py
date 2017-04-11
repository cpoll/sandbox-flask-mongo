"""
    Methods used for user login and token auth.
"""

from pymongo import MongoClient
from datetime import datetime, timedelta
from random import random

class Authentication:

    __TOKEN_LENGTH = 100
    __VALID_TOKEN_CHARACTERS = "abcdefghijklmnopqrstuvwxyz1234567890"

    def __init__(self):
        mongo_client = MongoClient('mongodb://localhost:27017/')
        db = mongo_client.test_database
        self.sessions = db.sessions


    """
        Given valid username/password pair, returns auth token. Else returns False
    """
    def authenticate(self, username, password):
        if username == password:
            token = self.__create_token()

            session_entry = {
                "token" : token,
                "date" : datetime.now()
            }
            self.sessions.insert_one(session_entry)

            return token
        else:
            return False;


    """
        Given a token, returns whether the token is valid
    """
    def verify_session(self, token):
        session = self.sessions.find_one({"token": token})
        return session and self.__verify_session_validity(session)

    @staticmethod
    def __verify_session_validity(session):
        return session["date"] and session["date"] > (datetime.now() - timedelta(days=1))

    def __create_token(self):
        return ''.join(map(lambda x: random.choice(self.__VALID_TOKEN_CHARACTERS), range(self.__TOKEN_LENGTH)))
