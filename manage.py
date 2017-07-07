from flask import current_app
from flask_script import Manager

from cafe import app
from cafe.database.database import db

manager = Manager(app)


@manager.command
def recreate_database():
    current_app.logger.info("Recreates database...")
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
