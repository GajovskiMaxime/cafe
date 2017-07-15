import datetime

from cafe.database.database import db


class Event(db.Model):

    __tablename__ = "APPOINTMENT"

    _columns_properties = {
        'id': 'ID',
        'label': 'LABEL',
        'description': 'DESCRIPTION',
        'location': 'LOCATION',
        'status': 'STATUS',
        'created_at': 'CREATED_AT'}

    id = db.Column(_columns_properties['id'], db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(_columns_properties['label'], db.String(), nullable=False)
    description = db.Column(_columns_properties['description'], db.String(), nullable=False)
    location = db.Column(_columns_properties['location'], db.Boolean(), nullable=False)
    status = db.Column(_columns_properties['status'], db.String(), nullable=False)
    created_at = db.Column(_columns_properties['created_at'], db.DateTime, nullable=False)

    def __init__(self, label, description, location):
        self.label = label
        self.description = description
        self.location = location
        self.created_at = datetime.datetime.now()

    @property
    def serialize(self):
        return {
            self._columns_properties['id'].lower(): self.id,
            self._columns_properties['label'].lower(): self.label,
            self._columns_properties['description'].lower(): self.description,
            self._columns_properties['location'].lower(): self.location,
            self._columns_properties['status'].lower(): self.status,
            self._columns_properties['created_at'].lower(): self.created_at,
        }
