from flask import abort, request
from flask_login import current_user, login_user
from datetime import timedelta

from functools import wraps
from .auth.models import UserAccountToken, UserAccount

def token_authorise(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                return f(*args, **kwargs)
            elif "Username" in request.headers:
                username = request.headers["Username"].replace('"', '')
                token = request.headers["User-Token"].replace('"', '')

                print(">>>>>>>>>", len(username))
                uat = UserAccountToken.query.filter_by(username=username).first()
                if uat is not None and uat.verify_token(token):

                    login_user(UserAccount.query.filter_by(id = uat.account_id).first())
                    return f(*args, **kwargs)
                else:
                    abort(401)
            abort(401)
    return decorated_function