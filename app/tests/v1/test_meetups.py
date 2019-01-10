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


class TestMeetups(BaseTest):
    """
    The tests for meetups"""

    def test_create_meetup_record(self):
        """Function to test creation of a meetup record"""
        url = '/api/v1/meetup/create'

        response= self.client.post(url, data=json.dumps(self.meetup), content_type="application/json")
        result = json.loads(response.data.decode('UTF-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [
            {
                "id": 1,
                "createdOn": createdOn,
                "topic": "Data Science Meetup, Nairobi",
                "location": "Nairobi",
                "images": ["datascience.png", "python.png"],
                "happeningOn": "Tuesday 1 2015",
                "tags": ["data", "python"]
            }
        ])

if __name__ == '__main__':
    unittest.main()