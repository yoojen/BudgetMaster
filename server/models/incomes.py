# creates user model

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Income(BaseModel, Base):
    __tablename__ = 'incomes'
    name = Column(String(60), nullable=False)
    desc = Column(String(60))
    amount = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category_id = Column(String(60), ForeignKey(
        'categories.id'), nullable=False)

    def __init__(self, name, amt, usrid, ctid):
        self.name = name
        self.amount = amt
        self.user_id = usrid
        self.category_id = ctid

    def __repr__(self) -> str:
        return f"{self.id}: {self.id}"
