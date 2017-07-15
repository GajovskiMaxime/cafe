import datetime

from sqlalchemy import Integer, String, Boolean, DateTime

from cafe.database.database import db


class User(db.Model):

    __tablename__ = "USER"

    _columns_properties = {
        'id': {
            'name': 'ID',
            'type_': Integer,
            'primary_key': True,
            'autoincrement': True
        },
        'username': {
            'name': 'USERNAME',
            'type_': String(128),
            'nullable': False
        },
        'email': {
            'name': 'EMAIL',
            'type_': String(128),
            'nullable': False
        },
        'is_active': {
            'name': 'IS_ACTIVE',
            'type_': Boolean,
            'default': False,
            'nullable': False
        },
        'created_at': {
            'name': 'CREATED_AT',
            'type_': DateTime,
            'nullable': False
        }
    }

    mandatory_fields_for_post = (
        _columns_properties['username']['name'],
        _columns_properties['email']['name']
    )

    id = db.Column(**_columns_properties['id'])
    username = db.Column(**_columns_properties['username'])
    email = db.Column(**_columns_properties['email'])
    is_active = db.Column(**_columns_properties['is_active'])
    created_at = db.Column(**_columns_properties['created_at'])

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now()

    @property
    def serialize(self):
        return {
            self._columns_properties['id']['name'].lower(): self.id,
            self._columns_properties['username']['name'].lower(): self.username,
            self._columns_properties['email']['name'].lower(): self.email,
            self._columns_properties['created_at']['name'].lower(): self.created_at,
        }
