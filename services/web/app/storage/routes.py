from flask_login import login_required

from . import storage
from .views import site_schema, sites_schema
from .models import Site
from .. import db

from ..decorators import token_authorise

@storage.route("/")
def storage_index():
    return "Hello World"

@storage.route("/api/sites/")
@token_authorise
def sites():
    all_sites = db.session.query(Site).all()
    return {"results": sites_schema.dump(all_sites)}

@storage.route("/api/sites/<id>")
@token_authorise
def site_detail(id):
    site = db.session.query(Site).filter(Site.id == id).first()
    return site_schema.dump(site)

@storage.route("/api/sites/new", methods=["POST"])
@token_authorise
def add_site():
    return "Hello World"