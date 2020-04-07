from sqlalchemy import Column
from backend import db


class UserClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable = False)
    eventID = db.Column(db.Integer, nullable = False)

    def __init__(self, userID, eventID):
        self.userID = userID
        self.eventID = eventID