from models.category import category
from flask import Blueprint, jsonify, request
from . import api
from requests import get
@api.route('/category', methods=['GET'])
def get_category():
    category_1= category().select_all(None)
    return jsonify(category_1)
@api.route('/category/percentage', methods=['GET'])
def get_category_percentage():
    category_1= category().select_all(None)
    d={}
    for i in category_1:
        d[i[1]]=float(i[2].replace('%',''))
    return jsonify(d)