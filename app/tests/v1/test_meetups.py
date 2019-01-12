"""
Tests for the meetups are defined here"""

import unittest
import json

from app import create_app


class BaseTest(unittest.TestCase):

    """
    The base test that occurs before any other test"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.meetup1 = {
            "topic": "Data Science Meetup, Nairobi",
            "location": "Nairobi",
            "images": ["datascience.png", "python.png"],
            "happeningOn": "Tuesday 1 2015",
            "tags": ["data", "python"]
        }
        self.meetup2 = {
            "topic": "Flask Restful",
            "location": "Nairobi",
            "images": ["flask.png", "flask-restful.png"],
            "happeningOn": "Tuesday 2 2018",
            "tags": ["data", "python"]
        }


class TestMeetups(BaseTest):
    """
    The tests for meetups"""

    def test_create_meetup_record(self):
        """Function to test creation of a meetup record"""
        url = '/api/v1/meetups'

        response = self.client.post(url, data=json.dumps(self.meetup1),
                                    content_type="application/json")
        result = json.loads(response.data.decode('UTF-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["status"], 201)
        self.assertEqual(result["data"], [
            {
                "topic": "Data Science Meetup, Nairobi",
                "location": "Nairobi",
                "happeningOn": "Tuesday 1 2015",
                "tags": ["data", "python"]
            }
        ])

    def test_fetch_all_upcoming_meetups(self):
        """Function to test API can fetch all upcoming meetups"""
        meetups_url = '/api/v1/meetups'
        all_meetups_url = '/api/v1/meetups/upcoming'

        # Post a second meetup(meetup2)
        post_response = self.client.post(meetups_url,
                                         data=json.dumps(self.meetup2),
                                         content_type="application/json")
        self.assertEqual(post_response.status_code, 201)

        # Fetch all meetups
        get_all_response = self.client.get(all_meetups_url)
        self.assertEqual(get_all_response.status_code, 200)

       
if __name__ == '__main__':
    unittest.main()
