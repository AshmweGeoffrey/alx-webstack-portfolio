from models.inventory_model import inventory
from flask import Blueprint, jsonify, request
from . import api
@api.route('/inventory', methods=['GET'])
def get_inventory():
    order="ORDER BY incoming_time_stamp DESC"
    inventory_1= inventory().select_all(order)
    return jsonify(inventory_1)