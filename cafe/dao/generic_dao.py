from flask import current_app

from cafe import create_app
from cafe.exceptions.database.empty_table_exception import EmptyTableException


class GenericDAO:

    def __init__(self, table):
        self.__table = table

    def read_all_without_filters_dao(self, session):
        with create_app().app_context():
            try:
                objects = session.query(self.__table).all()
                if not objects:
                    err = EmptyTableException(table=self.__table)
                    current_app.logger.warning(err.serialize)
                    raise err
            except EmptyTableException as err:
                raise err
            return objects
