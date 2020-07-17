import marshmallow_sqlalchemy as masql
from .. import ma
from .models import Site, FixedColdStorage

class SiteSchema(masql.SQLAlchemySchema):
    class Meta:
        model = Site
        load_instance = True

    id = masql.auto_field()
    name = masql.auto_field()
    created_on = masql.auto_field()
    created_by = masql.auto_field()


site_schema = SiteSchema()
sites_schema = SiteSchema(many=True)

class FixedColdStorageSchema(masql.SQLAlchemySchema):
    class Meta:
        model = FixedColdStorage

    id = masql.auto_field()
    name = masql.auto_field()
    created_on = masql.auto_field()

fcs_schema = FixedColdStorageSchema()
fcscomma_schema = FixedColdStorageSchema(many=True)