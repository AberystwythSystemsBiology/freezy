from . import panel
from flask_login import login_required, login_user, logout_user, current_user

from flask import render_template, flash

@panel.route("/")
@login_required
def index():
    return "Hello World"