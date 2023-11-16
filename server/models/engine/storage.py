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


def get_total(obj, type=""):
    objec_dc = {}
    data = get_single_ob(obj)
    for d in data:
        if d.to_dict().get("amount"):
            objec_dc[d.to_dict().get(type)] = d.to_dict().get("amount")
    return objec_dc


def get_obj_category(obj, type=""):
    obj_forID = []
    object = get_single_ob(obj)
    for instance in object:
        category_id = instance.to_dict().get('category_id')
        obj_name = instance.to_dict().get(type)
        if category_id:
            obj_forID.append({obj_name: category_id})
    return obj_forID


def categoriesOfExpenses(obj, type):
    objToReturn = []
    all_read = []
    for obj_cat in get_obj_category(obj, type):
        for cate in obj_cat.values():
            if cate not in all_read:
                all_read.append(cate)
                all_category = session.query(Category).filter(
                    Category.id == cate).first()
                if type == "income":
                    incomeByCategory = all_category.income
                    for one_category_item in incomeByCategory:
                        objToReturn.append(
                            {all_category.type: one_category_item.to_dict()})
                else:
                    expenseByCategory = all_category.expense
                    for one_category_item in expenseByCategory:
                        objToReturn.append(
                            {all_category.type: one_category_item.to_dict()})
    return objToReturn


def find_exp_category(cls, obj_id):
    obj = get_objectByID(cls, obj_id)
    if len(obj) < 1:
        return []
    for one_obj in obj:
        cate = one_obj.get('category_id')
        expense = session.query(cls).filter(
            cls.category_id == cate).first()
        return expense


def amount_gt(cls, amount, type):
    all_items = []
    if isinstance(amount, int):
        exp = session.query(cls).filter(cls.amount >= amount).all()
        for one in exp:
            date = "{}".format(datetime.datetime.strftime(
                one.date_updated, "%Y-%m-%d"))
            categories = session.query(Category).filter(
                Category.id == one.category_id).first()
            if type == "income":
                all_items.append(
                    {"name": one.name, "amount": one.amount, "date_updated": date, "category": categories.type})
            else:
                all_items.append(
                    {"name": one.name, "amount": one.amount, "date_updated": date, "category": categories.type})

        return all_items
    return []


def amount_lt(cls, amount, type):
    all_items = []
    if isinstance(amount, int):
        exp = session.query(cls).filter(cls.amount <= amount).all()
        for one in exp:
            date = "{}".format(datetime.datetime.strftime(
                one.date_updated, "%Y-%m-%d"))
            categories = session.query(Category).filter(
                Category.id == one.category_id).first()
            if type != "income":
                all_items.append(
                    {"name": one.name, "amount": one.amount, "date_updated": date, "category": categories.type})
            else:
                all_items.append(
                    {"name": one.name, "amount": one.amount, "date_updated": date, "category": categories.type})
        return all_items
    return []


def filter_obj_byDate(cls, date_range_1, date_range_2):
    try:
        data = []
        first_date = datetime.datetime.strptime(date_range_1, '%Y-%m-%d')
        last_date = datetime.datetime.strptime(date_range_2, '%Y-%m-%d')
        expenses = session.query(cls).filter(
            cls.date_updated.between(first_date, last_date)).all()
        for one_exp in expenses:
            # print(one_exp.to_dict()['date_updated'])
            # print(type(one_exp.to_dict().keys()))
            categories = session.query(Category).filter(
                Category.id == one_exp.category_id).first()
            if one_exp.to_dict()['date_updated']:
                one_exp.to_dict()['date_updated'] = datetime.datetime.strftime(
                    one_exp.to_dict()['date_updated'], "%Y-%m-%d")
                one_exp.to_dict()['category'] = categories.type
            data.append(one_exp.to_dict())
        return {"expenses <{}> - <{}>"
                .format(datetime.datetime.strftime(first_date, "%Y-%m-%d"),
                        datetime.datetime.strftime(last_date, "%Y-%m-%d")): data}
    except ValueError as e:
        return ({"error": str(e)})
