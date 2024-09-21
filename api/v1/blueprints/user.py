from models.user import user
from datetime import datetime
from flask import Blueprint, jsonify, request
from . import api
# [Discontinued]!! And not recommended to use(old sql )
@api.route('/user/<string:user_name>', methods=['GET'])
def get_user(user_name):
    user_1= user().get_user(user_name)
    user_1.append(datetime.now())
    return jsonify(user_1)