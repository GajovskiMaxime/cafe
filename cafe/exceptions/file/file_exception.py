class FileException(Exception):

    def __init__(self):
        super(FileException, self)

    @property
    def serialize(self):
        return {}

