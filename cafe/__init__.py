import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from cafe.api.user_controller import user_blueprint

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    app.register_blueprint(user_blueprint)

    return app