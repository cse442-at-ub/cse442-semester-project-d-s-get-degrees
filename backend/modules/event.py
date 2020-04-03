from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy import Column
from  backend import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String, nullable = True)

    def __init__(self, title, description):
        self.title = title
        self.description = description