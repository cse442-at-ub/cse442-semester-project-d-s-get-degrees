from sqlalchemy import Column
from backend import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    logo = db.Column(db.String)
    description = db.Column(db.String)
    players = db.Column(db.String)
    game = db.Column(db.String)

    def __init__(self, name, logo, description, players, game):
        self.name = name
        self.logo = logo
        self.description = description
        self.players = players
        self.game = game