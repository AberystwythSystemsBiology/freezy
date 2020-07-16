
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db, login_manager

class UserAccount(UserMixin, db.Model):
    __tablename__= "user_accounts"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(32), nullable=False, unique=True)
    password_hash = db.Column(db.String(256))

    is_admin = db.Column(db.Boolean, default=False)

    creation_date = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def password(self) -> AttributeError:
        raise AttributeError("No.")

    @password.setter
    def password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> None:
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id: int) -> UserAccount:
    return db.session.query(UserAccount).filter(UserAccount.id == user_id).first()