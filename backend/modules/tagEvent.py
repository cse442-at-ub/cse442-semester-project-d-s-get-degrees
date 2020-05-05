from backend import db


class TagEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagID = db.Column(db.Integer, nullable = False)
    eventID = db.Column(db.Integer, nullable = False)

    def __init__(self, tagID, eventID):
        self.tagID = tagID
        self.eventID = eventID