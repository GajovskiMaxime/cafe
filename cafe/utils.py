from flask import jsonify, make_response


def json_response(response):
    return make_response(jsonify(response)), response['status']
