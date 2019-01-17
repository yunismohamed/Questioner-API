"""Validators are defined here"""
import re
from app.api.v1.models.users_model import ALL_USERS


class UserValidator():
    """User details are validated here"""

    def is_valid_email(self, email):
        """Checks valid email format"""
        rex = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(rex, email)

    def is_valid_username(self, username):
        """Checks valid name format"""
        rex = "^[a-zA-Z]{3,}$"
        return re.match(rex, username)

    def is_valid_password(self, password):
        """Checks valid password format"""
        rex = "^[a-zA-Z0-9@_+-.]{3,}$"
        return re.match(rex, password)

    def email_exists(self, email):
        """Method for checking if user email exist"""
        user = [user for user in ALL_USERS if user['email'] == email]
        if user:
            return True
        return False

    def username_exists(self, username):
        """Method for checking if username exist"""
        user = [user for user in ALL_USERS if user['username'] == username]
        if user:
            return True
        return False
