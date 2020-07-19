import marshmallow_sqlalchemy as masql
from marshmallow import Schema, fields
from .. import ma

from .models import Site, FixedColdStorage, Shelf, Drawer, Box

from ..auth.views import UserAccountSchema, BasicAccountSchema

class DrawerSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Drawer

    id = masql.auto_field()
    name = masql.auto_field()
    size = masql.auto_field()
    created_on = masql.auto_field()
    shelf_id = masql.auto_field()

drawer_schema = DrawerSchema()
drawers_schema = DrawerSchema(many=True)

class ShelfSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Shelf

    id = masql.auto_field()
    name = masql.auto_field()
    created_on = masql.auto_field()
    shelves = ma.Nested(DrawerSchema, many=True)

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("storage.shelf_detail", id="<id>"), "collection": ma.URLFor("storage.shelves")}
    )

shelf_schema = ShelfSchema()
shelves_schema = ShelfSchema(many=True)

class FixedColdStorageSchema(masql.SQLAlchemySchema):
    class Meta:
        model = FixedColdStorage

    id = masql.auto_field()
    name = masql.auto_field()
    temperature = masql.auto_field()
    shelves = ma.Nested(ShelfSchema, many=True)

    site_id = masql.auto_field()

    # TODO: Setup marshmallow-enum
    type = fields.String()
    created_on = masql.auto_field()
    created_by = masql.auto_field()

    _links = ma.Hyperlinks(
        {"self": ma.URLFor("storage.fixed_cold_storage_detail", id="<id>"), "collection": ma.URLFor("storage.fixed_cold_storage")}
    )


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
    creator = ma.Nested(BasicAccountSchema)

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

