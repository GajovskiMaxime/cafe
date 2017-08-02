from flask import current_app
from numpy import genfromtxt

from cafe import create_app
from cafe.database.database import get_session
from cafe.models.user import User
from cafe.models.utils import table_name
from cafe.utils.path_utils import get_csv_path_from_table_name


# TODO verify if file exist.
# TODO verify if it's csv file.
# TODO verify if csv isn't malformed.
def load_data_from_csv(file_name):
    data = genfromtxt(file_name, delimiter=';', skip_header=1, dtype=None)
    return data.tolist()


def user_csv_to_sql():
    with create_app().app_context():
        session = get_session()
        try:

            file_name = get_csv_path_from_table_name(User)
            current_app.logger.info('Opening file : {}.'.format(file_name))
            data = load_data_from_csv(file_name)

            for attr in data:
                record = User(
                    username=attr[0].decode('utf-8'),
                    email=attr[1].decode('utf-8'),
                    password=attr[2].decode('utf-8'),
                    longitude=attr[3],
                    latitude=attr[4])

                session.add(record)
            session.commit()
            current_app.logger.info('Rows inserted successfully in table {}.'.format(table_name(User)))
        except OSError as err :
            current_app.logger.error('Something wrong occurs in the database')
            session.rollback()
        finally:
            session.close()