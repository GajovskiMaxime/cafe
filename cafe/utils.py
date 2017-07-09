from flask import jsonify, make_response


def default_success_dict_response():
    return {
        'status': '200',
        'data': ''
    }


def json_response(response):
    return make_response(jsonify(response)), response['status']
