from datetime import datetime

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from app import db
from blog.views import blog
from models import User
from users.forms import RegisterForm, LoginForm


users_blueprint = Blueprint('users', __name__, template_folder='templates')


def register():
    form = RegisterForm()

    if form.validate_on_submit():
        # if this returns a user, then the email already exists in database
        user = User.query.filter_by(username=form.username.data).first()

        # if a user is found redirect user back to signup page so user can try again
        if user:
            flash('Username address already exists')
            return render_template('register.html', form=form)

        # create a new user with the form data
        new_user = User(username=form.username.data,
                        password=form.password.data,
                        pinkey=form.pinkey.data)

        db.session.add(new_user)
        db.session.commit()

        return login()

        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again')

            return render_template('login.html', form=form)

        login_user(user)

        user.last_logged_in = user.current_logged_in
        user.current_logged_in = datetime.now()
        db.session.add(user)
        db.session.commit()

        return blog()
    return render_template('login.html', form=form)

@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))