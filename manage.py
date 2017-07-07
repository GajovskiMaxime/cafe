import unittest

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

@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('cafe/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
