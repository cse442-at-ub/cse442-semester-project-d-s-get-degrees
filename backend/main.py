from flask import Blueprint, render_template, send_from_directory,request
from flask_login import login_required, current_user
from backend.modules.event import Event
from backend.modules.userEvent import UserEvent
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
    return json.dumps(reversed(mds))

@main.route('/profile')
@login_required
def profile():
    userEvents = UserEvent.query.filter_by(userID=current_user.id)
    events = []
    for event in userEvents:
        events.append(Event.query.filter_by(id=event.eventID).first())
    return render_template('profile.html', name=current_user.firstName+" "+current_user.lastName, events = events , template_folder='../frontend')





