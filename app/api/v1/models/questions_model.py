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
            "body": body,
            "votes": 0
        }

        ALL_QUESTIONS.append(new_question)

    def upvote_question(self, id):
        question = [question for question in self.db if question["id"] == id]

        if not question:
            return False

        question[0]["votes"] += 1

        return {
            "meetup": question[0]["meetup"],
            "title": question[0]["title"],
            "body": question[0]["body"],
            "votes": question[0]["votes"]
        }

    def downvote_question(self, id):
        question = [question for question in self.db if question["id"] == id]

        if not question:
            return False

        question[0]["votes"] -= 1

        return {
            "meetup": question[0]["meetup"],
            "title": question[0]["title"],
            "body": question[0]["body"],
            "votes": question[0]["votes"]
        }