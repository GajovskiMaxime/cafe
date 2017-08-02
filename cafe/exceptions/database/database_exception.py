from cafe.exceptions.service_exception import ServiceException


class DatabaseException(ServiceException):

    def __init__(self):
        super(DatabaseException, self)
