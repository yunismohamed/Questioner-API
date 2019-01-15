"""
The rsvp models are defined here"""

RSVP = []  # DB of all rsvps


class Rsvp:

    """
    Contains models for the rsvp"""

    def __init__(self):
        """
        Initializes the rsvp class
        """
        self.db = RSVP

    def set_rsvp(self, meetup_id, user_id, response):
        """
        Sets the rsvp status for a meetup and adds it to the DB
        """
        rsvp = {
            "id": len(self.db) + 1,
            "meetup": meetup_id,
            "user": user_id,
            "response": response
        }

        RSVP.append(rsvp)
