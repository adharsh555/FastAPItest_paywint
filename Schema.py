From pydantic import BaseModel

class ExpenseCreate(BaseModel):
    id:int,
    name:str,
    amount:float,
    

class ExpenseResponse(ExpenseCreate):
    id:int,
    name:str,
    amount:float,
    category:str,
    date:date

    class config:
        from_attributes = True

class SalaryCreate(BaseModel):
    amount: float
    
class SalaryResponse(BaseModel):
    id:int,
    amount:float,
    date:date

    class config:
        from_attributes = True