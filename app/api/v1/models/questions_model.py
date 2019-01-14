"""
The questions models are defined here"""


from datetime import datetime

ALL_QUESTIONS = []  # DB of all questions


class Questions:

    """
    Contains models for the questions"""

    def __init__(self):
        """
        Initializes the questions class
        """
        self.db = ALL_QUESTIONS

    def add_question(self, userid, meetupid, title, body):
        pass