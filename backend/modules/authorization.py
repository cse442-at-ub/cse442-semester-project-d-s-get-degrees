from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from backend.modules.user import User
from backend.modules.event import Event
from backend.modules.userEvent import UserEvent
from .. import db
from flask.json import jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    if not user and check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
    return render_template('sign-up.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    lastName = request.form.get('lastName')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, firstName=firstName, lastName=lastName, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(url_for('main.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':

        eventID = request.json['eventID']
        userID = current_user.get_id()

        print('\n')
        print('POST REQUEST VALUES:')
        print('eventID : ' + eventID)
        print('userID : ' + userID)
        print('\n')

        # if userEvent exists in database, remove it; else, add it.
        userEvent = UserEvent.query.filter(UserEvent.userID == userID, UserEvent.eventID == eventID).first()
        db.session.rollback()

        print(userEvent)

        if userEvent:
            UserEvent.query.filter(UserEvent.userID == userID, UserEvent.eventID == eventID).delete()
            db.session.commit()
            return jsonify({'message' : 'success'})
        else:
            newUserEvent = UserEvent(userID, eventID)
            db.session.add(newUserEvent)
            db.session.commit()
            return jsonify({'message' : 'success'})

    else: # if request.method == 'GET'
        event = Event.query.all()
        return render_template('events.html', event=event)