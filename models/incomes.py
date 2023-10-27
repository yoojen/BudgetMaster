#creates user model

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Income(BaseModel, Base):
    __tablename__ = 'incomes'
    income = Column(String(60), nullable=False)
    cash_type = Column(String(60), nullable=False, default="Cash")
    desc = Column(String(60))
    amount = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)

    def __init__(self, name, pyme, amt, usrid, ctid):
        self.income = name
        self.cash_type = pyme
        self.amount = amt
        self.user_id = usrid
        self.category_id = ctid