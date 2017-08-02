from cafe.database.database import db
from cafe.models_properties.user_properties import UserProperties
from cafe.utils.models_utils import column_name


class User(db.Model):

    __tablename__ = "USER"

    properties = UserProperties()

    id = db.Column(**properties.get('id'))
    username = db.Column(**properties.get('username'))
    email = db.Column(**properties.get('email'))
    password = db.Column(**properties.get('password'))
    longitude = db.Column(**properties.get('longitude'))
    latitude = db.Column(**properties.get('latitude'))
    created_at = db.Column(**properties.get('created_at'))

    def __init__(self, username, email, password,
                 longitude=None, latitude=None):
        self.username = username
        self.email = email
        self.password = password
        self.longitude = longitude
        self.latitude = latitude

    @property
    def serialize(self):
        return {
            column_name(User, 'id'):        self.id,
            column_name(User, 'username'):  self.username,
            column_name(User, 'email'):     self.email,
            column_name(User, 'password'):  self.password,
            column_name(User, 'longitude'): self.longitude,
            column_name(User, 'latitude'):  self.latitude,
            column_name(User, 'created_at'):self.created_at,
        }
