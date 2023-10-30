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

from flask import request
from api.bm.views import bm_views
from models.engine import *
from flask import jsonify, abort
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
    expense_list = get_total(Expense)
    for values in expense_list.values():
        sum = sum + int(values)
    return jsonify(get_total(Expense), {"total expenses": sum})


@bm_views.route('/expenses/categories')
def expenses_categories():
    """returns category that is spent"""
    res = categoriesOfExpenses()
    return jsonify(res)


@bm_views.route('/expenses/<int:expense_id>/category')
def exp_category(expense_id):
    expense = find_exp_category(expense_id)
    if expense:
        return jsonify({str(expense.expense): [{"expense": expense.spend.type}]})
    return jsonify({"null": "yes"})


@bm_views.route('/expenses/amt_gt/<int:amount>')
def get_exp_amt_gt(amount):
    all_items = amount_gt(amount)
    return jsonify({"expenses amount >= {}".format(amount): all_items})


@bm_views.route('/expenses/amt_lt/<int:amount>')
def get_exp_amt_lt(amount):
    all_items = amount_lt(amount)
    return jsonify({"expenses amount <= {}".format(amount): all_items})


@bm_views.route('/expenses/date/<string:date_range_1>/<string:date_range_2>')
def filter_by_date(date_range_1, date_range_2):
    first_date = datetime.datetime.strptime(date_range_1, '%Y-%m-%d')
    last_date = datetime.datetime.strptime(date_range_2, '%Y-%m-%d')
    expenses = session.query(Expense).filter(
        Expense.date_updated.between(first_date, last_date)).all()
    print(expenses)

    return jsonify({"date": "...fettching"})
