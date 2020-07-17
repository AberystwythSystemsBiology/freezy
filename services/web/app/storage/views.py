import marshmallow_sqlalchemy as masql
from marshmallow import Schema, fields
from .. import ma

from .models import Site, FixedColdStorage, Shelf, Drawer, Box

class FixedColdStorageSchema(masql.SQLAlchemySchema):
    class Meta:
        model = FixedColdStorage

    id = masql.auto_field()
    name = masql.auto_field()
    created_on = masql.auto_field()


fcs_schema = FixedColdStorageSchema()
fcscomma_schema = FixedColdStorageSchema(many=True)

class SiteSchema(masql.SQLAlchemySchema):

    class Meta:
        model = Site

    id = masql.auto_field()
    name = masql.auto_field()
    storage = ma.Nested(FixedColdStorageSchema, many=True)
    created_on = masql.auto_field()
    created_by = masql.auto_field()

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("storage.site_detail", id="<id>"), "collection": ma.URLFor("storage.sites")}
    )

site_schema = SiteSchema()
sites_schema = SiteSchema(many=True)



class ShelfSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Shelf

    id = masql.auto_field()
    name = masql.auto_field()
    created_on = masql.auto_field()

shelf_schema = ShelfSchema()
shelves_schema = ShelfSchema(many=True)


class DrawerSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Drawer

    id = masql.auto_field()
    name = masql.auto_field()
    size = masql.auto_field()
    created_on = masql.auto_field()

drawer_schema = DrawerSchema()
drawers_schema = DrawerSchema(many=True)

class BoxSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Box

    id = masql.auto_field()
    name = masql.auto_field()
    rows = masql.auto_field()
    cols = masql.auto_field()
    created_on = masql.auto_field()

box_schema = BoxSchema()
boxes_schema = BoxSchema(many=True)

