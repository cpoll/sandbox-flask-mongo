"""
    Wrapper for mongo connections
"""

from pymongo import MongoClient
import os


class ConnectionWrapper:

    def __init__(self):
        mongo_client_key = 'flask_mongo_test_client'
        mongo_db_key = 'flask_mongo_test_db'

        assert mongo_client_key in os.environ
        assert mongo_db_key in os.environ

        mongo_client = MongoClient(os.environ[mongo_client_key])
        self.__db = mongo_client[os.environ[mongo_db_key]]

    def get_collection(self, collection):
        return self.__db[collection]