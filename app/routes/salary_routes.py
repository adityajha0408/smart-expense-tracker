from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, auth, optimizer
from ..services import salary_service

router = APIRouter(prefix="/salary", tags=["Salary"])

@router.post("/")
def set_salary(salary: schemas.SalaryBase, db: Session = Depends(database.SessionLocal),
               current_user=Depends(auth.get_current_user)):
    return salary_service.set_salary(db, salary, current_user.id)

@router.get("/optimize/")
def optimize_salary(db: Session = Depends(database.SessionLocal),
                    current_user=Depends(auth.get_current_user)):
    return optimizer.analyze_expenses(db)
