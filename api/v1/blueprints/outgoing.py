from flask import Blueprint, jsonify, request
from models.outgoing_stock import outgoing_stock
from . import api
@api.route('/out_going', methods=['GET'])
def get_out_going():
    order="ORDER BY time_stamp DESC"
    out_going1= outgoing_stock().select_all(order)
    return jsonify(out_going1)