import os

SQLALCHEMY_DATABASE_URI = "sqlite:///{path}".format(
    path=os.environ["SQLALCHEMY_DATABASE_URI"]
)

SECRET_KEY = os.environ["SECRET_KEY"]
WTF_CSRF_SECRET_KEY = os.environ["WTF_CSRF_SECRET_KEY"]