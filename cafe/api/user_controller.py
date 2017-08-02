from flask import Blueprint, request, jsonify

from cafe.exceptions.service_exception import ServiceException
from cafe.services.user_services import UserService
from cafe.utils.json_utils import json_response

user_blueprint = Blueprint(
    'users',
    __name__,
    url_prefix='/users')


@user_blueprint.route('/', methods=['GET'])
def get_all_users_route():

    is_lazy = False
    args = request.args.to_dict()
    user_service = UserService()

    try:
        if 'lazy' in request.args:
            args.pop('lazy', None)
            is_lazy = True

        response = user_service.\
            get_without_filters_service(
                is_lazy=is_lazy)

    except ServiceException as err:
        return json_response(**err.serialize)
    return jsonify(response)
