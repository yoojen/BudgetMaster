#creates user model

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Expense(BaseModel, Base):
    __tablename__ = 'expenses'
    expense = Column(String(60), nullable=False)
    desc = Column(String(60))
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    
    def __init__(self, name, amt, usrid, ctid):
        self.expense = name
        self.amount = amt
        self.user_id = usrid
        self.category_id = ctid

    def __repr__(self):
        return f"<{self.__tablename__}>: <{self.expense}>"