# creates user model

from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = "users"
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    fname = Column(String(60), nullable=False)
    lname = Column(String(60), nullable=False)
    password = Column(String(18), nullable=False)
    location_id = Column(String(60), ForeignKey('location.id'), nullable=False)
    expense = relationship("Expense", backref='users')
    income = relationship("Income", backref="users")

    def __init__(self, usrname, email, fname, lname, psd, loc_id):
        self.username = usrname
        self.email = email
        self.fname = fname
        self.lname = lname
        self.password = psd
        self.location_id = loc_id
