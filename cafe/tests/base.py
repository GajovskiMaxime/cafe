from unittest import TestCase

from cafe import app
from cafe.database.database import db


class BaseTestCase(TestCase):

    @staticmethod
    def create_app():
        app.config.from_object('cafe.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
