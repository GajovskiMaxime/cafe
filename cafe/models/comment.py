import datetime

from cafe.database.database import db


class Comment(db.Model):

    __tablename__ = 'COMMENT'

    _columns_properties = {
        'id': 'ID',
        'body': 'BODY',
        'sender': 'SENDER',
        'receiver': 'RECEIVER',
        'created_at': 'CREATED_AT',
        'last_edit': 'LAST_EDIT'}

    id = db.Column(_columns_properties['id'], db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(_columns_properties['body'], db.String(), nullable=False)
    sender = db.Column(_columns_properties['sender'], db.Integer, nullable=False)
    receiver = db.Column(_columns_properties['receiver'], db.Integer, nullable=False)
    created_at = db.Column(_columns_properties['created_at'], db.DateTime, nullable=False)
    last_edit = db.Column(_columns_properties['last_edit'], db.DateTime, nullable=False)

    def __init__(self, body, sender, receiver):
        self.body = body
        self.sender = sender
        self.receiver = receiver
        self.created_at = datetime.datetime.now()
        self.last_edit = self.created_at

    @property
    def serialize(self):
        return {
            self._columns_properties['id'].lower(): self.id,
            self._columns_properties['body'].lower(): self.body,
            self._columns_properties['sender'].lower(): self.sender,
            self._columns_properties['receiver'].lower(): self.receiver,
            self._columns_properties['created_at'].lower(): self.created_at,
            self._columns_properties['last_edit'].lower(): self.last_edit,
        }
