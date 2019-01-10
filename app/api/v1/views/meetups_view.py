"""
Responses to requests regarding meetups are set up here"""

from flask import Blueprint, request, jsonify

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

@v1.route("/meetups", methods=['POST'])  

