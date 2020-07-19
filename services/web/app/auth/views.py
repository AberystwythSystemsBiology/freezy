import marshmallow_sqlalchemy as ma
from .models import UserAccount

class UserAccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserAccount

    id = ma.auto_field()
    username = ma.auto_field()
    created_on = ma.auto_field()
    is_admin = ma.auto_field()


user_schema = UserAccountSchema()
users_schema = UserAccountSchema(many=True)

class BasicAccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserAccount

    id = ma.auto_field()
    username = ma.auto_field()

basic_user_schema = BasicAccountSchema()
basic_users_schema = BasicAccountSchema(many=True)