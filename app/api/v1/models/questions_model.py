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

    def add_question(self, createdBy, meetup, title, body):
        """
        Saves new question to to all questions DB
        """
        new_question = {
            "id": len(self.db) + 1,
            "createdOn": datetime.now(),
            "createdBy": createdBy,
            "meetup": meetup,
            "title": title,
            "body": body            
        }

        ALL_QUESTIONS.append(new_question)