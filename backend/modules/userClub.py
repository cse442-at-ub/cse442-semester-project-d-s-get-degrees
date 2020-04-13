from sqlalchemy import Column
from backend import db


class UserClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable = False)
    clubID = db.Column(db.Integer, nullable = False)

    def __init__(self, userID, clubID):
        self.userID = userID
        self.clubID = clubID