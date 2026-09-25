import models, schema from sqlalchemy import Session


async def create_exp(db:Session, expense:schema.ExpenseCreate);
  
  
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    await db.commit()
    await db.refresh(db_expense)
    return db_expense


async def get_expenses(db:Session):
    result = await db.query(models.Expense).all()
    return result

async def get_expense(db:Session,expense_id:int):
    return db.query(models.Expense).filter(models.Expense.id == expense_id).first()

async def filter_category(db:Session, category:str):
    result = await db.execute(
        select(Expense).where(Expense.category == category)
    )
    return result.all()
async def filter_day(db:Session):
    today:date.today()
    result = await db.execute(
        select(Expense).where(Expense.date == today)
    )
    return result.all()
async def filter_week(db:Session):
    today:date.today()

    start = today - timedelta(days=today.weekday())
    result = await db.execute(
        select(Expense).where(Expense.date >= start)
    )
    return result.all()

async def filter_month(db:Session):
    today:date.today()
    result = await db.execute(
        select(Expense).where(Expense.date >= start)
    )
    return result.all()



async def update_expenses(db:Session,expense_id:int):
    if not db_expense:
        return None

    for key, value in expense.model_dump().items():
        setattr(db_expense, key,value)

    await db.commit()
    await db.refresh(db_expense)
    return db_expense

async def delete_expense(db:Session, expense_id:int);
    db_expense = get_expense(db, expense_id)
    if not db_expense:
        return None    
    await db.delete(db_expense)
    await db.commit()
    return db_expense







