"""
    Methods used for user registration / login.
"""

from pymongo import MongoClient
import bcrypt


class Accounts:

    def __init__(self):
        mongo_client = MongoClient('mongodb://localhost:27017/')
        db = mongo_client.test_database
        self.accounts = db.accounts


    """
        Given a username/password pair, creates the user.
    """
    def create_user(self, username, password):

        if not username or not password:
            return False

        user = self.accounts.find_one({"username": username})
        if user:
            return False

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        new_account = {
            "username": username,
            "hashed_password": hashed_password,
            "salt": salt
        }

        self.accounts.insert_one(new_account)

        return True



    """
        Given a username/password pair, returns whether the user is valid
    """
    def verify_user(self, username, password):

        user = self.accounts.find_one({"username": username})
        if not user:
            return False

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), user["salt"])

        return hashed_password == user["hashed_password"]

"""
TODO: Turn into integration tests
if __name__ == "__main__":
    a = Accounts()

    print(a.create_user("cristian", "changeme"))
    print(a.verify_user("cristian", "changeme"))
    print(a.verify_user("cristian", "badpass"))
    print(a.verify_user("lala", "lala"))
    print(a.create_user("cristian", "changeme"))
"""
