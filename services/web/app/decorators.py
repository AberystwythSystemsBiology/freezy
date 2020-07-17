from flask import abort, request
from flask_login import current_user, login_required

from functools import wraps
from .auth.models import UserAccountToken

def token_authorise(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                return f(*args, **kwargs)
            elif "Username" in request.headers:
                username = request.headers["Username"]
                token = request.headers["User-Token"]
                uat = UserAccountToken.query.filter_by(username=username).first()

                if uat is not None and uat.verify_token(token):
                    return f(*args, **kwargs)
                else:
                    abort(401)
            abort(401)
    return decorated_function