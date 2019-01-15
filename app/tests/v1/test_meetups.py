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
        self.question1 = {
            "createdBy": 1,
            "meetup": 1,
            "title": "Python Data Science",
            "body": "What are the best tutorials for python data science?",
            "votes": 0
        }
        self.rsvp = {
            "user_id": 1,
            "response": "yes"
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
        self.assertIn("Data Science Meetup, Nairobi", str(result["data"]))

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

    def test_get_specific_meetup_record(self):
        """Function to test API can fetch specific meetup record"""

        # Post meetup2
        post_response = self.client.post('/api/v1/meetups',
                                         data=json.dumps(self.meetup2),
                                         content_type="application/json")
        self.assertEqual(post_response.status_code, 201)

        get_meetup_id_response = self.client.get('/api/v1/meetups/2')
        self.assertEqual(get_meetup_id_response.status_code, 200)
        self.assertIn("Flask Restful", str(get_meetup_id_response.data))

    def test_create_question(self):
        """
        Function to test API can create a question
        for a specific meetup
        """
        meetups_url = '/api/v1/meetups'
        questions_url = '/api/v1/questions'
        # Post meetup2
        response = self.client.post(meetups_url, data=json.dumps(self.meetup2),
                                    content_type="application/json")
        # Test meetup2 was posted successfully
        self.assertEqual(response.status_code, 201)
        # Post a question1 for meetup2
        questions_response = self.client.post(questions_url,
                                              data=json.dumps(self.question1),
                                              content_type="application/json")
        # Test question1 was posted successfully
        self.assertEqual(questions_response.status_code, 201)
        self.assertIn("Python Data Science", str(questions_response.data))

    def test_upvote_question(self):
        """
        Function to test API can upvote a specific question
        """
        meetups_url = '/api/v1/meetups'
        upvote_url = 'api/v1/questions/1/upvote'
        # Post meetup2
        response = self.client.post(meetups_url, data=json.dumps(self.meetup2),
                                    content_type="application/json")
        # Test meetup2 was posted successfully
        self.assertEqual(response.status_code, 201)

        upvote_response = self.client.patch(upvote_url,
                                            content_type='application/json')

        # Test the upvote patch was successful
        self.assertEqual(upvote_response.status_code, 202)

    def test_downvote_question(self):
        """
        Function to test API can downvote a specific question
        """
        meetups_url = '/api/v1/meetups'
        downvote_url = 'api/v1/questions/1/downvote'
        # Post meetup2
        response = self.client.post(meetups_url, data=json.dumps(self.meetup2),
                                    content_type="application/json")
        # Test meetup2 was posted successfully
        self.assertEqual(response.status_code, 201)

        downvote_response = self.client.patch(downvote_url,
                                              content_type='application/json')

        # Test the downvote patch was successful
        self.assertEqual(downvote_response.status_code, 202)

    def test_rsvp(self):
        """
        Function to test API can set rsvp status for a meetup
        """
        meetups_url = '/api/v1/meetups'
        rsvp_url = 'api/v1/meetups/2/rsvps'
        # Post meetup2
        response = self.client.post(meetups_url, data=json.dumps(self.meetup2),
                                    content_type="application/json")
        # Test meetup2 was posted successfully
        self.assertEqual(response.status_code, 201)

        # Post rsvp
        rsvp_response = self.client.post(rsvp_url, data=json.dumps(self.rsvp),
                                         content_type='application/json')

        # Test rsvp was set successfully
        self.assertEqual(rsvp_response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
