# define all class properties
from sqlalchemy import Column, String, DateTime, Integer, UUID
import datetime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid

Base = declarative_base()


class BaseModel:
    """
    this class defines properties that other classes will inherit
    """
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    date_created = Column(DateTime, nullable=False,
                          default=datetime.datetime.utcnow())
    date_updated = Column(DateTime, nullable=False,
                          default=datetime.datetime.utcnow())

    def save(self):
        """
        save instance to db
        """
        models.session.add(self)
        models.session.commit()

    def __str__(self):
        return f'{self.id}'

    def to_dict(self):
        instance_dict = self.__dict__
        if '_sa_instance_state' in instance_dict.keys():
            del instance_dict['_sa_instance_state']
        return instance_dict
