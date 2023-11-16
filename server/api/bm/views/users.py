from flask import jsonify
from models import *

"""
This module creates view for users in the db
All routes for user belongs here
"""
from models.engine import *
from api.bm.views import bm_views


@bm_views.route('/users', methods=['GET'], strict_slashes=False)
def get_or_post_user():
    """this methods is used to GET and POST methods for users"""
    return jsonify(get_object(User))


@bm_views.route('/users/<int:user_id>',  strict_slashes=False)
def user_byId(user_id):
    """return expense based on ID"""
    return jsonify(get_objectByID(User, user_id))


@bm_views.route('/users/<int:user_id>/expenses')
def user_expenses(user_id):
    objToReturn = []
    users = session.query(User).filter(User.id == user_id).first()
    if users:
        for user in users.expense:
            objToReturn.append(user.to_dict())
        return jsonify({users.username: objToReturn})
    return jsonify({"null": "yes"}), 404


@bm_views.route('/users/<int:user_id>/expenses/category')
def user_exp_categories(user_id):
    objToReturn = []
    """returns category that is spent"""
    res = categoriesOfExpenses(Expense, "expense")

    for exp in res:
        for k, v in exp.items():
            if v.get('user_id') == user_id:
                if k not in objToReturn:
                    objToReturn.append(
                        {"category id-> {}".format(v.get('category_id')): k})
    return jsonify({"categories": objToReturn})


@bm_views.route('/users/<int:user_id>/expenses/category/<int:categoryid>')
def user_exp_by_category(user_id, categoryid):
    objToReturn = []
    cate = None
    users = session.query(User).filter(User.id == user_id).first()
    for user in users.expense:
        if user.category_id == categoryid:
            objToReturn.append(user.to_dict())
            cate = session.query(Category).filter(
                Category.id == user.category_id).first().type

    return jsonify({cate: objToReturn})


@bm_views.route('/users/<int:user_id>/incomes')
def user_incomes(user_id):
    objToReturn = []
    users = session.query(User).filter(User.id == user_id).first()
    if users:
        for user in users.income:
            objToReturn.append(user.to_dict())
        return jsonify({users.username: objToReturn})
    return jsonify({"null": "yes"}), 404


@bm_views.route('/users/<int:user_id>/incomes/category')
def user_income_categories(user_id):
    objToReturn = []
    """returns category that is spent"""
    res = categoriesOfExpenses(Income, "income")
    for exp in res:
        for k, v in exp.items():
            if v.get('user_id') == str(user_id):
                if k not in objToReturn:
                    objToReturn.append(
                        {"category id-> {}".format(v.get('category_id')): k})
    return jsonify({"categories": objToReturn})


@bm_views.route('/users/<int:user_id>/incomes/category/<int:categoryid>')
def user_income_by_category(user_id, categoryid):
    objToReturn = []
    cate = None
    users = session.query(User).filter(User.id == user_id).first()
    for user in users.income:
        if user.category_id == str(categoryid):
            objToReturn.append(user.to_dict())
            cate = session.query(Category).filter(
                Category.id == user.category_id).first().type

    return jsonify({cate: objToReturn})
