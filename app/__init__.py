"""
App is created here
"""

from flask import Flask


from .api.v1.views.meetups_view import v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    return app
