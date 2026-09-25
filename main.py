
app = FastAPI()

@app.post("/expenses, status_code=201")
async def add_expense(expense: schema.ExpenseCreate,db:Session = Depends(get_db)):
    return await crud.create_expense(db, expense)


@app.post("/salary, status_code=201")
async def add_salary(salary: schema.SalaryCreate,db:Session = Depends(get_db)):
    return await crud.create_salary(db, salary)

@app.get("/expenses", response_model=list[schema.ExpenseResponse])
async def all_expenses(db:Session = Depends(get_db)):
    return await crud.get_expenses(db)

@app.get("/expenses/category/{category}")
async def expense_category(
    category:str,
    db:Session = Depends(get_db)
):
    return await crud.filter_category(db, category)

@app.get("/expenses/day")
async def expense_day(
    db:Session = Depends(get_db)
):
    return await crud.filter_day(db)

@app.get("/expenses/week")
async def expense_week(
    db:Session = Depends(get_db)
):
    return await crud.filter_week(db)

@app.get("/expenses/month")
async def expense_month(
    db:Session = Depends(get_db)
):
    return await crud.filter_month(db)

@app.get(/summary/salary)
async def salary_total(db)