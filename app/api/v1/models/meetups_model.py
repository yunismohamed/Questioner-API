"""
The meetups models are defined here"""


from datetime import datetime

ALL_MEETUPS = []  # DB of all meetups


class Meetup:

    """
    Contains models for the meetups"""

    def __init__(self):
        """
        Initializes the meetup class
        """
        self.db = ALL_MEETUPS

    def add_meetup_record(self, topic, happeningOn, location, images, tags):
        """
        Saves new meetup to to all meetups DB
        """
        new_meetup = {
            "id": len(self.db) + 1,
            "topic": topic,
            "happeningOn": happeningOn,
            "location": location,
            "images": images,
            "tags": tags,
            "created_at": datetime.now()
        }

        ALL_MEETUPS.append(new_meetup)

    def fetch_all_upcoming_meetups(self):
        """
        Fetches all meetups from the DB
        """
        return self.db
