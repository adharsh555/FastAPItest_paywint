from sqlalchemy import Column, Integer,String
from database import Base


class Expense(Base):
    __tablename__ = "expense"
    id = Column(Integer, primary_key=True)
    name = Column(Stringtring, nullable=False),
    amount= Column(float,nullable=False),
    category=Column(String, nullable=False)