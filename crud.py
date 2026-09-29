from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from models import Expense, Salary
from datetime import date, timedelta


async def create_expense(db: AsyncSession, expense):
    new_expense = Expense(**expense.model_dump())
    db.add(new_expense)
    await db.commit()
    await db.refresh(new_expense)
    return new_expense


async def create_salary(db: AsyncSession, salary):
    new_salary = Salary(**salary.model_dump())
    db.add(new_salary)
    await db.commit()
    await db.refresh(new_salary)
    return new_salary


async def get_expenses(db: AsyncSession):
    result = await db.execute(select(Expense))
    return result.scalars().all()


async def filter_by_category(db: AsyncSession, category: str):
    result = await db.execute(
        select(Expense).where(Expense.category == category)
    )
    return result.scalars().all()


async def filter_by_day(db: AsyncSession):
    today = date.today()
    result = await db.execute(
        select(Expense).where(Expense.date == today)
    )
    return result.scalars().all()


async def filter_by_week(db: AsyncSession):
    today = date.today()
    start = today - timedelta(days=today.weekday())

    result = await db.execute(
        select(Expense).where(Expense.date >= start)
    )
    return result.scalars().all()


async def filter_by_month(db: AsyncSession):
    today = date.today()

    result = await db.execute(
        select(Expense).where(
            func.strftime("%Y-%m", Expense.date)
            == today.strftime("%Y-%m")
        )
    )
    return result.scalars().all()


async def total_expense(db: AsyncSession):
    result = await db.execute(select(func.sum(Expense.amount)))
    return result.scalar() or 0


async def total_salary(db: AsyncSession):
    result = await db.execute(select(func.sum(Salary.amount)))
    return result.scalar() or 0