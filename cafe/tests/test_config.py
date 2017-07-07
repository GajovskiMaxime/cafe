import unittest
from unittest import TestCase

from flask import current_app

from cafe import app


class TestDevelopmentConfig(TestCase):
    @staticmethod
    def create_app():
        app.config.from_object('cafe.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        app = self.create_app()
        self.assertTrue(app.config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@cafe_database:5432/cafe_dev'
        )


class TestTestingConfig(TestCase):
    @staticmethod
    def create_app():
        app.config.from_object('cafe.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        app = self.create_app()
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@cafe_database:5432/cafe_test'
        )


class TestProductionConfig(TestCase):
    @staticmethod
    def create_app():
        app.config.from_object('cafe.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        app = self.create_app()
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
