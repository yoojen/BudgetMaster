from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

# Create a SQLAlchemy engine and session
Base = declarative_base()
# Replace with your database connection string
engine = create_engine('sqlite:///relation.db', echo=True)


class Category(Base):
    """parent table to expenses"""

    __tablename__ = 'categories'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    expense = relationship("Expense", backref="expense")

    def __repr__(self):
        return f'<Category> : {self.name}'


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    def __repr__(self):
        return f'<Category> : {self.name}'


Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)
Session = scoped_session(session)
session = Session()
