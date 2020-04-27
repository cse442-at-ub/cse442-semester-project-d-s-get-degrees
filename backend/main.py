from flask import Blueprint, render_template, send_from_directory, request
from flask.json import jsonify
from flask_login import login_required, current_user
from backend.modules.event import Event
from backend.modules.userEvent import UserEvent
from backend.modules.club import Club
from backend.modules.userClub import UserClub
from backend.modules.team import Team


from . import db

import time
import os
import glob
import json

main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html")

@main.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../frontend/css', path)

@main.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../frontend/js', path)

@main.route('/blogs/<path:path>')
def send_blog(path):
    file = open("blogs/"+path, "r") 
    return file.read()

@main.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('../frontend/images', path)

@main.route("/favicon.ico")
def send_favicon():
    return send_from_directory('../frontend', "favicon.ico")


@main.route("/<path:path>")
def route(path):
    return render_template(path+".html", template_folder='../frontend')

@main.route('/teams')
def teams():
    teams = Team.query.all()
    return render_template("teams.html", teams = teams , template_folder='../frontend')

@main.route('/sendpost', methods = ['POST'])
def save_post():
    jsdata = request.form['javascript_data']
    print(jsdata)
    if(not os.path.exists("blogs/")):
        os.mkdir("blogs/") 
    f= open("blogs/"+str(int(time.time()))+".md","w+")
    f.write(jsdata)
    f.close()
    return jsdata

@main.route('/getpost')
def get_post():  
    mds=glob.glob("blogs/*.md")
    print(mds)
    return json.dumps(mds)




@main.route('/profile')
@login_required
def profile():
    userClubs = UserClub.query.filter_by(userID = current_user.id)
    userEvents = UserEvent.query.filter_by(userID = current_user.id)
    clubs = []
    events = []

    for club in userClubs:
        clubs.append(Club.query.filter_by(id = club.clubID).first())
    for event in userEvents:
        events.append(Event.query.filter_by(id=event.eventID).first())
    
    return render_template('profile.html', name=current_user.firstName+" "+current_user.lastName, events = events, clubs = clubs, profilePic=current_user.profilePic, template_folder='../frontend')


@main.route('/clubs', methods=['GET', 'POST'])
def clubs():
    if request.method == 'POST':
        clubID = request.json['clubID']
        userID = current_user.get_id()

        # if userEvent exists in database, remove it; else, add it.
        userClub = UserClub.query.filter(UserClub.userID == userID, UserClub.clubID == clubID).first()
        db.session.rollback()

        if userClub:
            UserClub.query.filter(UserClub.userID == userID, UserClub.clubID == clubID).delete()
            db.session.commit()
            return jsonify({'message' : 'success, item removed from database'})

        else:
            newUserClub = UserClub(userID, clubID)
            db.session.add(newUserClub)
            db.session.commit()

        return jsonify({'message' : 'success, item added to database'})

    else: # if request.method == 'GET'
        clubs = Club.query.all()
        userClub = UserClub.query.filter_by(userID = current_user.get_id())

        return render_template('clubs.html', clubs = clubs, userClub = userClub, otherButton = True)
