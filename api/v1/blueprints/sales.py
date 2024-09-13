from flask import Blueprint, jsonify, request
from models.sale_weekly import sale_weekly
from . import api
@api.route('/sales', methods=['GET'])
def get_sales():
    order="ORDER BY time_stamp DESC"
    sale_weekly_1= sale_weekly().select_all(order)
    return jsonify(sale_weekly_1)
