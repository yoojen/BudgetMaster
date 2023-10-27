from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""
from models.engine import *
from api.bm.views import bm_views
from flask import request

@bm_views.route('/users', methods=['GET'])
def get_or_post_user():
    """this methods is used to GET and POST methods for users"""
    return jsonify(get_object(User))