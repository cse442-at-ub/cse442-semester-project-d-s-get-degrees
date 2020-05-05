from backend import db


class TagTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagID = db.Column(db.Integer, nullable = False)
    teamID = db.Column(db.Integer, nullable = False)

    def __init__(self, tagID, teamID):
        self.tagID = tagID
        self.teamID = teamID