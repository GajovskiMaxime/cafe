import datetime

from cafe.database.database import db


class User(db.Model):

    __tablename__ = "USER"

    _fields_labels = ["ID", "USERNAME", "EMAIL", "IS_ACTIVE", "CREATED_AT"]

    id = db.Column(_fields_labels[0], db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(_fields_labels[1], db.String(128), nullable=False)
    email = db.Column(_fields_labels[2], db.String(128), nullable=False)
    active = db.Column(_fields_labels[3], db.Boolean(), default=False, nullable=False)
    created_at = db.Column(_fields_labels[4], db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now()

    @property
    def dict_repr(self):
        return {
            self._fields_labels[0].lower(): self.id,
            self._fields_labels[1].lower(): self.username,
            self._fields_labels[2].lower(): self.email,
            self._fields_labels[4].lower(): self.created_at,
        }
