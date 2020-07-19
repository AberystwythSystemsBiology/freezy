from flask import request, abort
from flask_login import current_user
import json

from . import storage
from .views import *

from .models import Site, FixedColdStorage, Shelf, Box, Drawer
from .. import db

from ..decorators import token_authorise

@storage.route("/api/site/", methods=["GET"])
@token_authorise
def sites():
    return {"results": sites_schema.dump(Site.query.all())}

@storage.route("/api/site/<id>", methods=["GET"])
@token_authorise
def site_detail(id):
    return site_schema.dump(Site.query.filter_by(id = id).first())

@storage.route("/api/fcs/", methods=["GET"])
@token_authorise
def fixed_cold_storage():
    return {"results": fcscomma_schema.dump(FixedColdStorage.query.all())}

@storage.route("/api/fcs/<id>", methods=["GET"])
@token_authorise
def fixed_cold_storage_detail(id):
    return fcs_schema.dump(FixedColdStorage.query.filter_by(id = id).first())

@storage.route("/api/shelf/", methods=["GET"])
@token_authorise
def shelves():
    return {"results": shelves_schema.dump(Shelf.query.all())}

@storage.route("/api/shelf/<id>", methods=["GET"])
@token_authorise
def shelf_detail(id):
    return shelf_schema.dump(Shelf.query.filter_by(id = id).first())

@storage.route("/api/drawer/", methods=["GET"])
@token_authorise
def drawers():
    return {"results": drawers_schema.dump(Shelf.query.all())}

@storage.route("/api/drawer/<id>", methods=["GET"])
@token_authorise
def drawer_detail(id):
    return drawer_schema.dump(Drawer.query.filter_by(id = id).first())

@storage.route("/api/box/", methods=["GET"])
@token_authorise
def box():
    return {"results": boxes_schema.dump(Box.query.all())}

@storage.route("/api/box/<id>", methods=["GET"])
@token_authorise
def box_detail(id):
    return box_schema.dump(Box.query.filter_by(id = id).first())

@storage.route("/api/add/<entity>", methods=["POST"])
@token_authorise
def add_storage_entity(entity):

    payload = request.json

    entities = {
        "shelf": Shelf,
        "fcs": FixedColdStorage,
        "site": Site,
        "box": Box,
        "drawer": Drawer
    }

    if entity not in entities.keys() or "id" in payload:
        abort(400)

    e = entities[entity](**payload)
    e.created_by = current_user.id

    db.session.add(e)
    db.session.commit()


    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@storage.route("/app/edit/<entity>/<id>", methods=["POST"])
@token_authorise
def edit_storage_entity(entity, id):
    pass