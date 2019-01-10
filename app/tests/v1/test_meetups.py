"""
Tests for the meetups are defined here"""

import unittest
import json
from datetime import datetime

from app import create_app

createdOn = datetime.now()


class BaseTest(unittest.TestCase):

    """
    The base test that occurs before any other test"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client        

        self.meetup = {
            "id": 1,
            "createdOn": createdOn,
            "topic": "Data Science Meetup, Nairobi",
            "location": "Nairobi",
            "images": ["datascience.png", "python.png"],
            "happeningOn": "Tuesday 1 2015",
            "tags": ["data", "python"]
        }


