"""
Responses to requests regarding meetups are set up here"""

from flask import Blueprint

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

