from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import *
from models.user import User
from models.category import Category
from models.expenses import Expense
from models.incomes import Income
from models.location import Location


classes = [User, Category, Expense, Income, Location]
engine = create_engine('sqlite:///budgetmaster.db', echo=False)
Base.metadata.create_all(bind=engine)

factory = sessionmaker(bind=engine, expire_on_commit=False)
Session = scoped_session(factory)
session = Session()


def get_single_ob(obj):
    if obj is None:
        return {"error": "Not Found"}
    data = session.query(obj).all()
    return data


def get_object(obj):
    obj_list = []
    data = get_single_ob(obj)
    for d in data:
        obj_list.append(d.to_dict())
    return obj_list


def get_objectByID(obj, id):
    obj_list = []
    data = get_single_ob(obj)
    for d in data:
        if d.to_dict().get('id') == id:
            obj_list.append(d.to_dict())
    return obj_list


def get_total(obj):
    objec_dc = {}
    data = get_single_ob(obj)
    for d in data:
        if d.to_dict().get("amount"):
            objec_dc[d.to_dict().get("expense")] = d.to_dict().get("amount")
    return objec_dc


def get_obj_category(obj):
    obj_forID = {}
    object = get_single_ob(obj)
    for instance in object:
        category_id = instance.to_dict().get('category_id')
        obj_name = instance.to_dict().get("expense")
        if category_id:
            obj_forID[obj_name] = category_id
    return obj_forID


def categoriesOfExpenses():
    objToReturn = []
    all_read = []
    obj_cat = get_obj_category(Expense).values()

    for cate in obj_cat:
        if cate not in all_read:
            all_read.append(cate)
            all_category = session.query(Category).filter(
                Category.id == cate).first()
            expenseByCategory = all_category.expense

            for one_category_item in expenseByCategory:
                objToReturn.append(
                    {all_category.type: one_category_item.to_dict()})
    return objToReturn

def find_exp_category(id):

    obj = get_objectByID(Expense, id)
    for one_obj in obj:
        cate = one_obj.get('category_id')
        expense = session.query(Expense).filter(
            Expense.id == cate).first()
        return expense


def amount_gt(amount):
    all_items = []
    exp = session.query(Expense).filter(Expense.amount >= amount).all()
    for one in exp:
        all_items.append({one.expense: one.amount})
    return all_items

def amount_lt(amount):
    all_items = []
    if isinstance(amount, int):
        exp = session.query(Expense).filter(Expense.amount <= amount).all()
        for one in exp:
            all_items.append({one.expense: one.amount})
        return all_items
    return []
