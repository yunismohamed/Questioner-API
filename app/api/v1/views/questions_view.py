"""
Responses to requests regarding questions are set up here"""

from flask import Blueprint, request, jsonify

from app.api.v1.models.questions_model import Questions

questions_v1 = Blueprint('questions_v1', __name__, url_prefix='/api/v1')

questions_obj = Questions()


@questions_v1.route("/questions", methods=['POST'])
def create_question():
    """
    Function to create a question
    """
    try:
        createdBy = request.get_json()['createdBy']
        meetup = request.get_json()['meetup']
        title = request.get_json()['title']
        body = request.get_json()['body']

    except:
        return jsonify({'status': 400,
                        'error': 'Invalid request format!'}), 400

    if not createdBy:
        return jsonify({'status': 400, 'error': 'Missing user ID field'}), 400

    if not meetup:
        return jsonify({
            'status': 400, 'error': 'Missing meetup ID field'}), 400

    if not title:
        return jsonify({'status': 400, 'error': 'Missing title field'}), 400

    if not body:
        return jsonify({'status': 400, 'error': 'Missing body field'}), 400

    questions_obj.add_question(createdBy, meetup, title, body)

    return jsonify({"status": 201,
                    "data": [{"user": createdBy,
                              "meetup": meetup,
                              "title": title,
                              "body": body}]}), 201


@questions_v1.route("/questions/<int:id>/upvote", methods=['PATCH'])
def upvote_question(id):
    """
    Function to upvote a question
    """
    upvoted_question = questions_obj.upvote_question(id=id)

    if not upvoted_question:
        return jsonify({
                "status": 404,
                "error": "Question not found"
            }), 404
    return jsonify({
        "status": 202,
        "data": [upvoted_question]
    }), 202


@questions_v1.route("/questions/<int:id>/downvote", methods=['PATCH'])
def downvote_question(id):
    """
    Function to downvote a question
    """
    downvoted_question = questions_obj.downvote_question(id=id)

    if not downvoted_question:
        return jsonify({
                "status": 404,
                "error": "Question not found"
            }), 404
    return jsonify({
        "status": 202,
        "data": [downvoted_question]
    }), 202
