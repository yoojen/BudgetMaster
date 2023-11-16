from flask import request
from api.bm.views import bm_views
from models.engine import *
from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


@bm_views.route('/categories', strict_slashes=False)
def categories():
    """returns all objects from db"""
    return jsonify(get_object(Category))


@bm_views.route('/categories/<int:category_id>',  strict_slashes=False)
def category_byId(category_id):
    """return expense based on ID"""
    return jsonify(get_objectByID(Category, category_id))


@bm_views.route('/categories/date/<string:date_range_1>/<string:date_range_2>')
def filter_category_by_date(date_range_1, date_range_2):
    data = filter_obj_byDate(Category, date_range_1, date_range_2)
    return jsonify(data)
