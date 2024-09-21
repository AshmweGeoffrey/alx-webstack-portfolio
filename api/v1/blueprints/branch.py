from models.branch import branch
from flask import Blueprint, jsonify, request
from . import api
@api.route('/branch', methods=['GET'])
def get_branch():
    # retrive branch_name from database
    branch_1= branch().select_all(order=None)
    return jsonify(branch_1)