from flask_login import UserMixin
from backend import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    profilePic = db.Column(db.String(1000))
    preferGame = db.Column(db.String(255))
    eventList = db.Column(db.String(255))