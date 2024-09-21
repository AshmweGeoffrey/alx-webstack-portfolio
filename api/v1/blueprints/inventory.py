from models.inventory_model import inventory
from flask import Blueprint, jsonify, request
from . import api
# api endpoint to get all inventory,order by incoming_time_stamp
@api.route('/inventory', methods=['GET'])
def get_inventory():
    # api endpoint to get all inventory,order by incoming_time_stamp
    order="ORDER BY incoming_time_stamp DESC"
    inventory_1= inventory().select_all(order)
    return jsonify(inventory_1)