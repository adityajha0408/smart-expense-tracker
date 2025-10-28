from sqlalchemy.orm import Session
from .. import models, schemas, utils

def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    if not expense.category:
        expense.category = utils.categorize_expense(expense.description)
    db_expense = models.Expense(**expense.dict(), owner_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def list_expenses(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.owner_id == user_id).all()

def delete_expense(db: Session, expense_id: int, user_id: int):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.owner_id == user_id).first()
    if exp:
        db.delete(exp)
        db.commit()
        return True
    return False

