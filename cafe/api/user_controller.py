from flask import Blueprint, request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from cafe import db
from cafe.models.user import User
from cafe.utils import json_response

user_blueprint = Blueprint('user',
                           __name__,
                           url_prefix='/users')


@user_blueprint.route('/', methods=['PUT'])
def add_user():

    json_request = request.get_json(force=True)
    try:
        fields = [json_request[item.lower()] for item in list(User.mandatory_fields_for_post)]
    except KeyError as k:
        return json_response({'status': 400, 'data': 'KeyError : attribute {} not found.'.format(k.args)})

    if '' in fields:
        return json_response({'status': 400, 'data': 'One of the attribute is empty.'})

    new_user = User(**json_request)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError as i:
        return json_response({'status': 400, 'data': 'IntegrityError : {}'.format(i.args)})
    except TypeError as t:
        return json_response({'status': 400, 'data': 'TypeError : {}'.format(t.args)})
    return json_response({'status': 200, 'data': 'Scenario \'{}\' added successfully.'.format(new_user.id)})


@user_blueprint.route('/', methods=['GET'])
def get_all_users():

    try:
        users = User.query.order_by(User.created_at.desc()).all()
        if not users:
            return json_response({'status': 404, 'data': 'No user found on database.'})

        users_list = []
        for user in users:
            users_list.append(user.serialize)

    except SQLAlchemyError as s:
        return json_response({'status': 400, 'data': 'SQLAlchemyError : {}'.format(s.args)})
    return json_response({'status': 200, 'data': {'users': users_list}})


@user_blueprint.route('/<user_id>', methods=['GET'])
def get_user_with_id(user_id):

    try:
        user = User.query.filter_by(id=int(user_id)).first()
        if not user:
            return json_response({'status': 404, 'data': 'No user found for id \'{}\'.'.format(user_id)})
    except ValueError:
        return json_response({'status': 400, 'data': 'Invalid id \'{}\'.'.format(user_id)})
    except SQLAlchemyError as s:
        return json_response({'status': 400, 'data': 'SQLAlchemyError : {}'.format(s.args)})
    return json_response({'status': 200, 'data': {'user': user.serialize}})
