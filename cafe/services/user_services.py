from cafe.models.user import User
from cafe.services.generic_services import GenericService


class UserService:

    def __init__(self):
        self.__generic_services = GenericService(User)

    def get_without_filters_service(self, is_lazy):
        return self.__generic_services.\
            get_without_filters_service(
                is_lazy=is_lazy)
