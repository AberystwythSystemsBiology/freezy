from . import auth
from .forms import LoginForm
from flask_login import login_required, login_user, logout_user, current_user

from flask import render_template, flash, redirect, url_for

from .. import db
from .models import UserAccount

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(UserAccount).filter(UserAccount.username == form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return "Logged in."
        else:
            flash("Incorrect username or password provided.")

    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    flash("You have successfully been logged out.")
    return redirect(url_for("auth.login"))