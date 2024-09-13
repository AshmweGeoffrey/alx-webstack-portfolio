from flask import Blueprint, jsonify, request
from models.remark import remark
from . import api
@api.route('/remarks', methods=['GET'])
def get_remarks():
    order="ORDER BY time_stamp DESC"
    remark_1= remark().select_all(order)
    return jsonify(remark_1)