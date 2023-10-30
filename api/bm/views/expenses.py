from api.bm.views import bm_views
from models.engine import *
from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


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
    expense_list = get_total(Expense, "expense")
    for values in expense_list.values():
        sum = sum + int(values)
    return jsonify(expense_list, {"total expenses": sum})


@bm_views.route('/expenses/categories')
def expenses_categories():
    """returns category that is spent"""
    res = categoriesOfExpenses(Expense, "expense")
    return jsonify(res)


@bm_views.route('/expenses/<int:expense_id>/category')
def exp_category(expense_id):
    expense = find_exp_category(Expense, expense_id)
    if expense:
        return jsonify({str(expense.expense): [{"category": expense.spend.type}]})
    return jsonify({"null": "yes"})


@bm_views.route('/expenses/amt_gt/<int:amount>')
def get_exp_amt_gt(amount):
    all_items = amount_gt(Expense, amount, "expense")
    return jsonify({"expenses amount >= {}".format(amount): all_items})


@bm_views.route('/expenses/amt_lt/<int:amount>')
def get_exp_amt_lt(amount):
    all_items = amount_lt(Expense, amount, "expense")
    return jsonify({"expenses amount <= {}".format(amount): all_items})


@bm_views.route('/expenses/date/<string:date_range_1>/<string:date_range_2>')
def filter_by_date(date_range_1, date_range_2):
    data = filter_obj_byDate(Expense, date_range_1, date_range_2)
    return jsonify(data)
