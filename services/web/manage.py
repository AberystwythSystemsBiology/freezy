from flask_script import Manager
from app import create_app, db

app = create_app()
manager = Manager(app)

from app.auth.models import UserAccount

@manager.command
def create_admin():
    with app.app_context():
        if UserAccount.query.filter_by(username="Admin").first() is None:
            user = UserAccount(
                username="Admin",
                password="adminpassword",
                is_admin=True
            )

            db.session.add(user)
            db.session.commit()
        else:
            print("NOTICE: Admin already exists.")

if __name__ == "__main__":
    manager.run()