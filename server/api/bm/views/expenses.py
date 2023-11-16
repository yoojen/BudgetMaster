from api.bm.views import bm_views
from models.engine import *
from flask import jsonify, request
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""


@bm_views.route('/expenses', methods=['GET', 'POST'], strict_slashes=False)
def expenses():
    """returns all objects from db"""
    data = []
    if (request.method == 'POST'):
        print("yes")
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        type = request.form['type']
        desc = request.form['desc']
        data.append(name)
        data.append(int(amount))
        data.append(1)
        data.append(int(category))
        print(type)
        if type == "expense":
            Expense(data[0], data[1], data[2], data[3]).save()
            return jsonify(message="data recorded successfully")
        elif type == "income":
            Income(data[0], data[1], data[2], data[3]).save()
            return jsonify(message="data recorded successfully")
    else:
        return jsonify(get_object(Expense))


@bm_views.route('/expenses/<string:name>',  strict_slashes=False)
def expense_byName(name):
    """return expense based on ID"""
    data = get_object(Expense)
    for exp in data:
        if exp.get('name').lower() == name:
            return jsonify(exp)


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
    # print(res)
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
    if (data):
        return jsonify(data)
    return []
