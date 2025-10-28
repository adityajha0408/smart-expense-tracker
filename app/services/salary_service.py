from sqlalchemy.orm import Session
from .. import models, schemas

def set_salary(db: Session, salary: schemas.SalaryBase, user_id: int):
    existing = db.query(models.UserSalary).filter(models.UserSalary.user_id == user_id).first()
    if existing:
        existing.monthly_salary = salary.monthly_salary
    else:
        existing = models.UserSalary(monthly_salary=salary.monthly_salary, user_id=user_id)
        db.add(existing)
    db.commit()
    db.refresh(existing)
    return existing

def get_salary(db: Session, user_id: int):
    return db.query(models.UserSalary).filter(models.UserSalary.user_id == user_id).first()
