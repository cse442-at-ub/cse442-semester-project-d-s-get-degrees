from flask import Blueprint, render_template, send_from_directory
from flask_login import login_required, current_user
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


@main.route("/<path:path>")
def route(path):
    return render_template(path+".html", template_folder='../frontend')

#
# @main.route("/clubs")
# def club():
#     return render_template("clubs.html", template_folder='../frontend')
#
#
# @main.route("/events")
# def events():
#     return render_template("events.html", template_folder='../frontend')
#
#
# @main.route("/teams")
# def teams():
#     return render_template("teams.html", template_folder='../frontend')
#
#
# @main.route("/sign-up")
# def signup():
#     return render_template("sign-up.html", template_folder='../frontend')
#
#
# @main.route("/login")
# def login():
#     return render_template("login.html", template_folder='../frontend')


# @main.route("/index")
# def login():
#     return render_template("login.html", template_folder='../frontend')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, template_folder='../frontend')





