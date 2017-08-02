import os

from flask import current_app
from numpy import genfromtxt

from cafe import create_app
from cafe.exceptions.file.file_format_exception import FileFormatException
from cafe.exceptions.file.file_not_found_exception import FileNotFoundException
from cafe.models.user import User
from cafe.path_utils import get_folder_path_from_root_project
from cafe.utils.models_utils import table_name


def get_csv_path_from_table_name(table):
    return get_folder_path_from_root_project('csv' + os.path.sep + table_name(table) + '.csv')


def load_data_from_csv(file_name):
    data = genfromtxt(
        file_name,
        skip_header=1,
        missing_values='',
        filling_values=0.0,
        delimiter=',',
        dtype=None)
    return data.tolist()


# TODO verify if csv isn't malformed.
# TODO verify if file exist.
# TODO verify if it's csv file.
def user_csv_to_sql(session):
    with create_app().app_context():
        file_path = None
        try:
            file_path = get_csv_path_from_table_name(User)
            current_app.logger.info('Opening file : {}.'.format(file_path))
            data = load_data_from_csv(file_path)

            for attr in data:
                record = User(**{
                        'username':     attr[0].decode('utf-8'),
                        'email':        attr[1].decode('utf-8'),
                        'password':     attr[2].decode('utf-8'),
                        'longitude':    float(attr[3]),
                        'latitude':     float(attr[4])
                })
                session.add(record)
            current_app.logger.info('Rows inserted successfully in table {}.'.format(table_name(User)))

        except (IndexError, ValueError) as err:
            raise FileFormatException(
                file_path=file_path,
                err=err)
        except OSError as err:
            if '.csv not found' in err.args[0]:
                raise FileNotFoundException(
                    file_path=file_path,
                    err=err)
