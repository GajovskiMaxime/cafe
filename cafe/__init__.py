import os

import logging
from flask import Flask
from cafe.database.database import db

from cafe.api.user_controller import user_blueprint


def create_app():

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    app.register_blueprint(user_blueprint)

    db.init_app(app)

    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    return app
