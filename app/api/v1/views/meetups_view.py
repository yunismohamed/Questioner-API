"""
Responses to requests regarding meetups are set up here"""

from flask import Blueprint, request, jsonify

from app.api.v1.models.meetups_model import Meetup

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

meetups_db = Meetup()


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
        return jsonify({'status': 400,
                        'error': 'Invalid request format!'}), 400

    if not topic:
        return jsonify({'status': 400, 'error': 'Missing topic field'}), 400

    if not happeningOn:
        return jsonify({
            'status': 400, 'error': 'Missing happeningOn field'}), 400

    if not location:
        return jsonify({'status': 400, 'error': 'Missing location field'}), 400

    if not tags:
        return jsonify({'status': 400, 'error': 'Missing tags field'}), 400

    meetups_db.add_meetup_record(topic, happeningOn, location, images, tags)

    return jsonify({"status": 201,
                    "data": [{"topic": topic,
                              "location": location,
                              "happeningOn": happeningOn,
                              "tags": tags}]}), 201


@v1.route("/meetups/upcoming", methods=['GET'])
def get_all_upcoming_meetups():
    """
    Function to fetch all upcoming meetups
    """
    all_upcoming_meetups = meetups_db.fetch_all_upcoming_meetups()

    if len(all_upcoming_meetups) == 0:
        return jsonify({
            "status": 404,
            "error": "There are no meetups created."
        }), 200
    return jsonify({
        "status": 200,
        "data": all_upcoming_meetups
    }), 200


    