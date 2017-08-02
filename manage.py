import unittest

from flask import current_app
from flask_script import Manager

from cafe import create_app, db
from cafe.database.database import get_session
from cafe.exceptions.file.file_exception import FileException
from cafe.utils.csv_utils import user_csv_to_sql

app = create_app()
manager = Manager(app)


@manager.command
def recreate_database():
    current_app.logger.info("Recreates database...")
    db.drop_all()
    db.create_all()
    populate_database()
    db.session.commit()


@manager.command
def populate_database():
    """Populates the database with csv files into stuart/csv/*.csv"""
    current_app.logger.info("Populating the database.")
    session = get_session()
    try:
        user_csv_to_sql(session)
        session.commit()
    except FileException as f:
        session.rollback()
        current_app.logger.error(f.serialize)
        exit()
    finally:
        session.close()


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
