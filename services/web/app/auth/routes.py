from . import auth
from .forms import LoginForm
from flask_login import login_required, login_user, logout_user, current_user

from flask import render_template, flash, redirect, url_for

from .. import db
from .models import UserAccount, UserAccountToken

from .views import user_schema, users_schema
from uuid import uuid4

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserAccount.query.filter_by(username=form.username.data).first()
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

@auth.route("/token")
@login_required
def update_token():
    token = str(uuid4())
    uat = UserAccountToken.query.filter_by(account_id=current_user.id).first()

    if uat != None:
        uat.token = token
    else:
        uat = UserAccountToken(
            username = current_user.username,
            account_id=current_user.id,
            token=token
        )

        db.session.add(uat)
    db.session.commit()

    return render_template("auth/token.html", token=token)


@auth.route("/api/accounts")
@login_required
def accounts():
    all_users = db.session.query(UserAccount).all()
    return {"results": users_schema.dump(all_users)}

@auth.route("/api/account/<attr>/<value>")
@login_required
def account(attr, value):
    user = db.session.query(UserAccount).filter(getattr(UserAccount, attr) == value).first()
    return user_schema.dump(user)
