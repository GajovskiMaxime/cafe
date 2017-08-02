from datetime import datetime

from flask import jsonify


def object_list_to_json(object_list, is_lazy):
    if is_lazy:
        return [item.serialize_lazy for item in object_list]
    return [item.serialize for item in object_list]


def json_response(**args):
    status_code = args['status']
    args.pop('status', None)
    response = jsonify({
        'datetime': datetime.now(),
        'status': status_code,
        'data': args,
    })
    return response, status_code

