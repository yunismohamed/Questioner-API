"""
Responses to requests regarding meetups are set up here"""

from flask import Blueprint, request, jsonify

from app.api.v1.models.meetups_model import Meetup

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

@v1.route("/meetups", methods=['POST'])
def create_meetup():
    """
    Function to create a meetup record
    """
    try:
        topic = request.get_json()['topic']
        happeningOn = request.get_json()['happeningOn']
        location = request.get_json()['location']
        images = request.get_json()['images']
        tags = request.get_json()['tags']

    except:
        return jsonify({'status':400,
                        'error': 'Invalid request format!'}), 400

    if not topic:
        return jsonify({'status':400, 'error':'Missing topic field'}), 400

    if not happeningOn:
        return jsonify({'status':400, 'error':'Missing happeningOn field'}), 400

    if not location:
        return jsonify({'status':400, 'error':'Missing location field'}), 400

    if not tags:
        return jsonify({'status':400, 'error':'Missing tags field'}), 400

    new_meetup = Meetup(
        topic=topic,
        happeningOn=happeningOn,
        location=location,
        images=images,
        tags=tags
    )

    new_meetup.add_meetup_record()

    


