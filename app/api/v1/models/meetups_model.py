"""
The meetups models are defined here"""


from datetime import datetime

ALL_MEETUPS = [] # DB of all meetups

class Meetup:
    """
    Contains models for the meetups
    """
    def __init__(self, topic, meetup_date, location, images, tags):
        """
        Initializes the meetup class
        """
        self.id = len(MEETUPS)+1
        self.topic = topic
        self.meetup_date = meetup_date
        self.location = location
        self.images = images
        self.tags = tags
        self.created_at = datetime.now()

    def save_meetup(self):
        """
        saves new meetup to to all meetups list
        """
        MEETUPS.append(self)