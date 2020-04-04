from sqlalchemy import Column
from backend import db


class User_Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable = False)
    eventID = db.Column(db.Integer, nullable = False)