from backend import db


class TagClub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagID = db.Column(db.Integer, nullable = False)
    clubID = db.Column(db.Integer, nullable = False)

    def __init__(self, tagID, clubID):
        self.tagID = tagID
        self.clubID = clubID