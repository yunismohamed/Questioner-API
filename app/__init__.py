"""
App is created here
"""

from flask import Flask


from .api.v1.views.meetups_view import v1
from .api.v1.views.questions_view import questions_v1
from .api.v1.views.users_view import auth


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(questions_v1)
    app.register_blueprint(auth)

    return app
