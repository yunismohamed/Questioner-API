"""
Responses to requests regarding questions are set up here"""

from flask import Blueprint, request, jsonify

from app.api.v1.models.questions_model import Questions

questions_v1 = Blueprint('questions_v1', __name__, url_prefix='/api/v1')



