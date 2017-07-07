from flask import Blueprint, jsonify

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })