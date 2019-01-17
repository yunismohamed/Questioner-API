"""
Responses to requests regarding users are set up here"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from app.api.v1.models.users_model import Users
from app.api.v1.utils.validators import UserValidator

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')
user_obj = Users()
validate = UserValidator()


@auth.route('/signup', methods=['POST'])
def signup():
    """ Allows signup of a new user """

    try:
        firstname = request.get_json()['firstname']
        lastname = request.get_json()['lastname']
        email = request.get_json()['email']
        username = request.get_json()['username']
        password = request.get_json()['password']
        role = request.get_json()['role']

    except:
        return jsonify({'status': 400,
                        'error': 'Invalid request format!'}), 400

    if not firstname:
        return jsonify({
            "status": 400,
            "error": "Firstname is missing!"
        }), 400
    if not lastname:
        return jsonify({
            "status": 400,
            "error": "Lastname is missing!"
        }), 400
    if not email:
        return jsonify({
            "status": 400,
            "error": "email is missing!"
        }), 400
    if not username:
        return jsonify({
            "status": 400,
            "error": "Username is missing!"
        }), 400
    if not password:
        return jsonify({
            "status": 400,
            "error": "Password is missing!"
        }), 400
    if not role:
        return jsonify({
            "status": 400,
            "error": "Role is missing!"
        }), 400

    if not validate.is_valid_password(password):
        return jsonify({
            "status": 400,
            "error": "Password not valid"
        }), 400

    if not validate.is_valid_email(email):
        return jsonify({
            "status": 400,
            "error": "Invalid email"
        }), 400

    if validate.username_exists(username):
        return jsonify({
            "status": 400,
            "error": "Username exists"
        }), 400

    if validate.email_exists(email):
        return jsonify({
            "status": 400,
            "error": "Email exists"
        }), 400
    hash_password = generate_password_hash(password)

    user_obj.add_user(firstname, lastname, email,
                      username, hash_password, role)
    return (jsonify({
        "status": 201,
        "data": [{
            "firstname": firstname,
            "username": username,
            "email": email,
            "role": role
        }]
    })), 201


@auth.route('/login', methods=['POST'])
def login():
    """
    Allows a user to login
    """

    try:
        username = request.get_json()['username']
        password = request.get_json()['password']
    except:
        return jsonify({'status': 400,
                        'error': 'Invalid request format!'}), 400

    if not username:
        return jsonify({
            "status": 400,
            "error": "Username is missing!"
        }), 400
    if not password:
        return jsonify({
            "status": 400,
            "error": "Password is missing!"
        }), 400

    # Check if the user exists
    valid_user = user_obj.check_user(username, password)

    if not valid_user:
        return jsonify({
            "status": 400,
            "error": "Username does not exist or incorrect password"
        }), 400
    return jsonify({
                "status": 200,
                "message": f"Successfully logged in as {username}"
        }), 200
