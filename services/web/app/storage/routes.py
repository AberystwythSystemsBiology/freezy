from flask import request
from flask_login import current_user
import json

from . import storage
from .views import site_schema, sites_schema
from .models import Site, FixedColdStorage, Shelf
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

@storage.route("/api/add/site", methods=["POST"])
@token_authorise
def add_site():
    r = request.json
    if "id" in r:
        site = Site.query.filter_by(id = r["id"]).first_or_404()
    else:
        site = Site()

    for i in request.json.keys():
        setattr(site, i, r[i])

    site.created_by = current_user.id
    db.session.add(site)
    db.session.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@storage.route("/api/add/fcs")
@token_authorise
def add_fixed_cold_storage():
    r = request.json
    if "id" in r:
        fcs = FixedColdStorage.query.filter_by(id=r["id"]).first_or_404()
    else:
        fcs = FixedColdStorage()

    for i in request.json.keys():
        setattr(fcs, i, r[i])

    fcs.created_by = current_user.id
    db.session.add(fcs)
    db.session.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@storage.route("/api/add/fcs")
@token_authorise
def add_shelf():
    r = request.json
    if "id" in r:
        s = Shelf.query.filter_by(id=r["id"]).first_or_404()
    else:
        s = Shelf()

    for i in request.json.keys():
        setattr(s, i, r[i])

    s.created_by = current_user.id
    db.session.add(s)
    db.session.commit()

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}