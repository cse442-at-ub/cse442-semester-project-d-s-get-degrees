from flask import Blueprint, render_template, send_from_directory, request
from flask.json import jsonify
from flask_login import login_required, current_user
from backend.modules.event import Event
from backend.modules.userEvent import UserEvent
main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("index.html")

@main.route('/css/<path:path>')
def send_js(path):
    return send_from_directory('../frontend/css', path)


@main.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('../frontend/images', path)

@main.route("/favicon.ico")
def send_favicon():
    return send_from_directory('../frontend', "favicon.ico")


@main.route("/<path:path>")
def route(path):
    return render_template(path+".html", template_folder='../frontend')


@main.route('/profile')
@login_required
def profile():
    userEvents = UserEvent.query.filter_by(userID=current_user.id)
    events = []
    for event in userEvents:
        events.append(Event.query.filter_by(id=event.eventID).first())
    return render_template('profile.html', name=current_user.firstName+" "+current_user.lastName, events = events , template_folder='../frontend')


@main.route('/clubs', methods=['GET', 'POST'])
def clubs():
    if request.method == 'POST':
        return jsonify({'message' : 'success'})

    else: # if request.method == 'GET'
        return render_template('clubs.html')
