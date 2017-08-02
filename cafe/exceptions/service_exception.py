
class ServiceException(Exception):

    def __init__(self):
        super(ServiceException, self)

    @property
    def serialize(self):
        return {}
