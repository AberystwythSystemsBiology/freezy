from flask import Blueprint

storage = Blueprint("storage", __name__)

from . import routes