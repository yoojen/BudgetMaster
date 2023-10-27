"""
    expenses
    (returns all expenses)

    expenses/<int:expense_id>
    expense/total (returns total expense)

    expense/categories
    (returns expenses categories)

    expense/category/<int:expense_id>
    (returns category for a certain expense)

    expenses/amt_gt/<float:amount>
    (get expenses where user paid more than a certain amount of money)
    
    expenses/amt_lt/<float:amount>
    (get expenses where user paid less than a certain amount of money)
"""

from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""
from models.engine import *
from api.bm.views import bm_views
from flask import request

@bm_views.route('/expenses', strict_slashes=False)
def expenses():
    """returns all objects from db"""
    return jsonify(get_object(Expense))

@bm_views.route('/expenses/<int:expense_id>',  strict_slashes=False)
def expense_byId(expense_id):
    """return expense based on ID"""
    return jsonify(get_objectByID(Expense, expense_id))


@bm_views.route('/expenses/total')
def total_expense():
    """returns total amount spent"""
    sum = 0
    expense_list = get_total(Expense)
    # for exp in expense_list:
    for values in expense_list.values():
        sum = sum + int(values)
    return jsonify(get_total(Expense), {"total expenses": sum})



    