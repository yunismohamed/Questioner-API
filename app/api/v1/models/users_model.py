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
