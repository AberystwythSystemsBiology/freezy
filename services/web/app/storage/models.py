from .. import db
from .enums import *

class Site(db.Model):
    __versioned__ = {}
    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

class FixedColdStorage(db.Model):
    __versioned__ = {}
    __tablename__ = "storage"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))


class Shelf(db.Model):
    __versioned__ = {}
    __tablename__ = "shelves"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    storage_id = db.Column(db.Integer, db.ForeignKey("storage.id"))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))



class Drawer(db.Model):
    __versioned__ = {}
    __tablename__ = "drawers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    shelf_id = db.Column(db.Integer, db.ForeignKey("shelves.id"))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

class Box(db.Model):
    __versioned__ = {}
    __tablename__ = "boxes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)

    shelf_id = db.Column(db.Integer, db.ForeignKey("shelves.id"))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))



class EntityToStorage(db.Model):
    __versioned__ = {}
    __tablename__ = "entity_to_storage"

    id = db.Column(db.Integer, primary_key=True)

    sample_id = db.Column(db.Integer)
    box_id = db.Column(db.Integer, db.ForeignKey("shelves.id"))
    shelf_id = db.Column(db.Integer, db.ForeignKey("shelves.id"))
    drawer_id = db.Column(db.Integer, db.ForeignKey("drawers.id"))
    storage_id = db.Column(db.Integer, db.ForeignKey("storage.id"))
    site_id = db.Column(db.Integer, db.ForeignKey("sites.id"))

    type = db.Column(db.Enum(EntityToStorageType), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

