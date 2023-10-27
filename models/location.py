#creates user model

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Location(BaseModel, Base):
    __tablename__ = 'location'
    country = Column(String(60), nullable=False)
    province = Column(String(60), nullable=False)
    user = relationship('User', backref='location')

    def __init__(self, ctr, pr):
        self.country = ctr
        self.province = pr
