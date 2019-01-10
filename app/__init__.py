"""
App is created here
"""

from flask import Flask

# Local import
from instance.config import app_config

from .api.v1.views.meetups_view import v1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)

    return app
