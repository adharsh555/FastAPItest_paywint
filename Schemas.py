from pydantic import BaseModel
from datetime import date


class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str


class ExpenseResponse(BaseModel):
    id: int
    name: str
    amount: float
    category: str
    date: date

    class Config:
        from_attributes = True


class SalaryCreate(BaseModel):
    amount: float


class SalaryResponse(BaseModel):
    id: int
    amount: float
    date: date

    class Config:
        from_attributes = True