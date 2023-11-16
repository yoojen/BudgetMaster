# creates user model

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Category(BaseModel, Base):
    __tablename__ = 'categories'
    type = Column(String(60), nullable=False)
    expense = relationship("Expense", backref="spend")
    income = relationship("Income", backref="revenue")

    def __init__(self, name):
        self.type = name
