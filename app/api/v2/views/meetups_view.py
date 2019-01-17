"""
Responses to requests regarding meetups are set up here"""

from flask import Blueprint, request, jsonify

from app.api.v1.models.meetups_model import Meetup
from app.api.v1.models.rsvp_model import Rsvp

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

meetups_obj = Meetup()
rsvp_obj = Rsvp()


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

    meetups_obj.add_meetup_record(topic, happeningOn, location, images, tags)

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
    all_upcoming_meetups = meetups_obj.fetch_all_upcoming_meetups()

    if len(all_upcoming_meetups) == 0:
        return jsonify({
            "status": 404,
            "error": "There are no meetups created."
        }), 404
    return jsonify({
        "status": 200,
        "data": all_upcoming_meetups
    }), 200


@v1.route("/meetups/<int:id>", methods=['GET'])
def get_specific_meetup(id):
    """
    Function to fetch specific meetup
    """
    meetup = meetups_obj.fetch_specific_meetup(id)
    if not meetup:
        return jsonify({
            "status": 404,
            "error": "Meetup does not exist."
        }), 404
    return jsonify({
        "status": 200,
        "data": meetup
    }), 200


@v1.route('/meetups/<int:id>/rsvps', methods=['POST'])
def add_rsvp(id):
    '''Adds RSVP for a meetup for a specific user'''

    meetup = meetups_obj.fetch_specific_meetup(id=id)

    if not meetup:
        return jsonify({
            "status": 404,
            "error": "Meetup does not exist."
        }), 404

    meetup_id = meetup[0]["id"]
    topic = meetup[0]["topic"]

    try:
        user_id = request.get_json()['user_id']
        response = request.get_json()['response']

    except:
        return jsonify({'status': 400,
                        'error': 'Invalid request format!'}), 400

    if not user_id:
        return jsonify({'status': 400, 'error': 'Missing user id field'}), 400
    if not response:
        return jsonify({'status': 400,
                        'error': 'Missing rsvp response field'}), 400

    rsvp_obj.set_rsvp(meetup_id, user_id, response)

    return jsonify({
                'status': 201,
                'data': [{
                    "meetup": meetup_id,
                    "topic": topic,
                    "status": response
                }]
            }), 201
