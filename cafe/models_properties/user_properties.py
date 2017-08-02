from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, Float


class UserProperties:

    __columns_properties = {
        'id': {
            'type_': Integer,
            'primary_key': True,
            'autoincrement': True
        },
        'username': {
            'type_': String,
            'nullable': False
        },
        'email': {
            'type_': String,
            'nullable': False
        },
        'password': {
            'type_': String,
            'nullable': False
        },
        'longitude': {
            'type_': Float,
            'nullable': True
        },
        'latitude': {
            'type_': Float,
            'nullable': True
        },
        'created_at': {
            'type_': DateTime,
            'nullable': False,
            'default': datetime.now()
        }
    }

    def __init__(self):
        for key, value in self.__columns_properties.items():
            value['name'] = key.upper()

    def get(self, key):
        return self.__columns_properties[key]
