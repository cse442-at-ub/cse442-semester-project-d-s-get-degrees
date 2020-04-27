from backend import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name