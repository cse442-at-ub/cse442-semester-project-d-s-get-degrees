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

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.firstName+" "+current_user.lastName, template_folder='../frontend')





