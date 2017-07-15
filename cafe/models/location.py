
from cafe.database.database import db


class Location(db.Model):

    __tablename__ = "LOCATION"

    _columns_properties = {
        'id': 'ID',
        'latitude': 'LATITUDE',
        'longitude': 'LONGITUDE'}

    id = db.Column(_columns_properties['id'], db.Integer, primary_key=True, autoincrement=True)
    latitude = db.Column(_columns_properties['latitude'], db.String(), nullable=False)
    longitude = db.Column(_columns_properties['longitude'], db.String(), nullable=False)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @property
    def serialize(self):
        return {
            self._fields_labels['id'].lower(): self.id,
            self._fields_labels['latitude'].lower(): self.latitude,
            self._fields_labels['longitude'].lower(): self.longitude,
        }
