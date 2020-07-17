import marshmallow_sqlalchemy as ma
from .models import Site

class SiteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Site

    id = ma.auto_field()
    name = ma.auto_field()


site_schema = SiteSchema()
sites_schema = SiteSchema(many=True)