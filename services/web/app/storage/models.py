from .. import db
from .enums import *

class Site(db.Model):
    __versioned__ = {}
    __tablename__ = "sites"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    storage = db.relationship("FixedColdStorage", backref="site")

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

class FixedColdStorage(db.Model):
    __versioned__ = {}
    __tablename__ = "storage"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)
    type = db.Column(db.Enum(ColdStorageType))
    temperature = db.Column(db.String(10))

    site_id = db.Column(db.Integer, db.ForeignKey("sites.id"))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))


class Shelf(db.Model):
    __versioned__ = {}
    __tablename__ = "shelves"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

class Drawer(db.Model):
    __versioned__ = {}
    __tablename__ = "drawers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)
    size = db.Column(db.Enum(DrawerSizes))

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))

class Box(db.Model):
    __versioned__ = {}
    __tablename__ = "boxes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(256), nullable=False)

    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    created_by = db.Column(db.Integer, db.ForeignKey("user_accounts.id"))