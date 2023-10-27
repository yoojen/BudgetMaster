from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import *
from models.user import User
from models.category import Category
from models.expenses import Expense
from models.incomes import Income
from models.location import Location


classes = [User, Category, Expense, Income, Location]
engine = create_engine('sqlite:///budgetmaster.db', echo=True)
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