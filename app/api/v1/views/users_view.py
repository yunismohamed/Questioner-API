"""
Responses to requests regarding users are set up here"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from app.api.v1.models.users_model import Users
from app.api.v1.utils.validators import UserValidator

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
user_obj = Users()
validate = UserValidator()


