"""
The meetups models are defined here"""


from datetime import datetime

ALL_MEETUPS = [] # DB of all meetups

class Meetup:
    """
    Contains models for the meetups
    """
    def __init__(self, topic, happeningOn, location, images, tags):
        """
        Initializes the meetup class
        """
        self.id = len(MEETUPS)+1
        self.topic = topic
        self.happeningOn = happeningOn
        self.location = location
        self.images = images
        self.tags = tags
        self.created_at = datetime.now()

    def add_meetup_record(self):
        """
        Saves new meetup to to all meetups list and returns the details
        """
        MEETUPS.append(self)

        # Returns the details of the new meetup
        return {
            "id": meetup.id,
            "topic": meetup.topic,
            "haoppeningOn": meetup.happeningOn,
            "location": meetup.location,
            "images": meetup.images,
            "tags": meetup.tags,
            "created_at": meetup.created_at
        }

    