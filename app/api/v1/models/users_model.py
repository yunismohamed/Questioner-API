import re
from werkzeug.security import generate_password_hash, check_password_hash

"""
The users models are defined here"""

ALL_USERS = []  # DB of all users


class Users:

    """
    Contains models for the users"""

    def __init__(self):
        """
        Initializes the rsvp class
        """
        self.db = ALL_USERS

    def add_user(self, firstname, lastname, email, username, password, role):
        """ Sets the details of the new user and adds the user to DB """

        new_user = {
            "id": len(self.db) + 1,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "username": username,
            "password": password,
            "role": role
        }

        ALL_USERS.append(new_user)

    def check_user(self, username, password):
        """
        Checks whether the username and password match"""
        user = [user for user in self.db if user['username'] == username]
        if user:
            if check_password_hash(user[0]["password"], password):
                return True
            return False
        return False
