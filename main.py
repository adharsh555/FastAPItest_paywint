from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import models, schemas, crud
from database import engine, Base, get_db

app = FastAPI(title="Expense Management API")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Create Expense
@app.post("/expenses", response_model=schemas.ExpenseResponse)
async def add_expense(
    expense: schemas.ExpenseCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_expense(db, expense)


# Create Salary
@app.post("/salary", response_model=schemas.SalaryResponse)
async def add_salary(
    salary: schemas.SalaryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_salary(db, salary)


# Get All Expenses
@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
async def all_expenses(db: AsyncSession = Depends(get_db)):
    return await crud.get_expenses(db)


# Filter by Category
@app.get("/expenses/category/{category}")
async def expenses_category(
    category: str,
    db: AsyncSession = Depends(get_db)
):
    return await crud.filter_by_category(db, category)


# Filter Today's Expenses
@app.get("/expenses/day")
async def expenses_day(db: AsyncSession = Depends(get_db)):
    return await crud.filter_by_day(db)


# Filter Weekly Expenses
@app.get("/expenses/week")
async def expenses_week(db: AsyncSession = Depends(get_db)):
    return await crud.filter_by_week(db)


# Filter Monthly Expenses
@app.get("/expenses/month")
async def expenses_month(db: AsyncSession = Depends(get_db)):
    return await crud.filter_by_month(db)


# Total Expense
@app.get("/summary/expense")
async def expense_total(db: AsyncSession = Depends(get_db)):
    total = await crud.total_expense(db)
    return {"total_expense": total}


# Total Salary
@app.get("/summary/salary")
async def salary_total(db: AsyncSession = Depends(get_db)):
    total = await crud.total_salary(db)
    return {"total_salary": total}


# Balance
@app.get("/summary/balance")
async def balance(db: AsyncSession = Depends(get_db)):
    salary = await crud.total_salary(db)
    expense = await crud.total_expense(db)

    return {
        "salary": salary,
        "expense": expense,
        "balance": salary - expense
    }