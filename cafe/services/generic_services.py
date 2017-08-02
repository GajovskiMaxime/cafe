from cafe.dao.generic_dao import GenericDAO
from cafe.database.database import get_session
from cafe.exceptions.database.database_exception import DatabaseException
from cafe.utils.json_utils import object_list_to_json
from cafe.utils.models_utils import table_name


class GenericService:

    def __init__(self, table):
        self.__table = table
        self.__dao = GenericDAO(table)

    def get_without_filters_service(self, is_lazy):
        session = get_session()
        try:
            response = self.__dao.\
                read_all_without_filters_dao(
                    session=session)
            json_list = object_list_to_json(response, is_lazy)
        except DatabaseException as err:
            raise err
        finally:
            session.close()
        return {str(table_name(self.__table) + 's'): json_list}

