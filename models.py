from sqlalchemy import Column, Integer, String, Float, Date
from datetime import date
from database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, default=date.today)


class Salary(Base):
    __tablename__ = "salary"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=date.today)