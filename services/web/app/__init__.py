import os

from flask import Flask, g, render_template
from config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from sqlalchemy import orm

from sqlalchemy_continuum import make_versioned
from sqlalchemy_continuum.plugins import FlaskPlugin
from sqlalchemy_continuum.plugins import PropertyModTrackerPlugin

db = SQLAlchemy()
login_manager = LoginManager()

make_versioned(plugins=[FlaskPlugin(), PropertyModTrackerPlugin()])

# Blueprints
from .auth import auth as auth_blueprint
from .panel import panel as panel_blueprint

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[os.environ["FLASK_CONFIG"]])
    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate = Migrate(app, db)

    orm.configure_mappers()

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Load in models here
    from .auth import models as auth_models

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(panel_blueprint)

    return app
