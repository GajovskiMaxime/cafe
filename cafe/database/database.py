from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


def get_session():
    engine = db.get_engine(app=current_app)
    Session = sessionmaker(
        bind=engine,
        autocommit=False,
        expire_on_commit=False)
    return Session()
