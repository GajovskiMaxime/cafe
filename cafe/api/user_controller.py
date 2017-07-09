from flask import Blueprint, jsonify, make_response, request, current_app
from sqlalchemy.exc import SQLAlchemyError

from cafe.database.database import db
from cafe.models.user import User
from cafe.utils import default_success_dict_response, json_response

user_blueprint = Blueprint('user', __name__, url_prefix='/users')

#
# @user_blueprint.route('/', methods=['POST'])
# def add_user():
#
#     post_data = request.get_json()
#     username = post_data.get('username')
#     email = post_data.get('email')
#     db.session.add(User(username=username, email=email))
#     db.session.commit()
#
#     response_object = {
#         'status': 'success',
#         'message': '{} was added!'.format(email)
#     }
#     return make_response(jsonify(response_object)), 201


@user_blueprint.route('/', methods=['GET'])
def get_all_users():

    response = default_success_dict_response()
    try:
        users = User.query.all()
        if not users:
            response['status'] = 204
            return json_response(response)

        users_list = []
        for user in users:
            user_dict_repr = user.dict_repr
            users_list.append(user_dict_repr)
        response['data'] = {'users': users_list}

    except SQLAlchemyError as s:
        response['status'] = 400
        response['data'] = ''.format(s.args)

    return json_response(response)


@user_blueprint.route('/<user_id>', methods=['GET'])
def get_user_with_id(user_id):

    response = default_success_dict_response()
    try:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            response['status'] = 204
            return json_response(response)

        response['data'] = {'user': user.dict_repr}

    except SQLAlchemyError as s:
        response['status'] = '400'
        response['data'] = ''.format(s)

    return json_response(response)
