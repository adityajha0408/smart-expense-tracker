from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
import shutil
from .. import database, schemas, utils, auth
from ..services import expense_service

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=schemas.Expense)
def add_expense(expense: schemas.ExpenseCreate,
                db: Session = Depends(database.SessionLocal),
                current_user=Depends(auth.get_current_user)):
    return expense_service.create_expense(db, expense, current_user.id)

@router.get("/")
def list_expenses(db: Session = Depends(database.SessionLocal),
                  current_user=Depends(auth.get_current_user)):
    return expense_service.list_expenses(db, current_user.id)

@router.delete("/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(database.SessionLocal),
                   current_user=Depends(auth.get_current_user)):
    success = expense_service.delete_expense(db, expense_id, current_user.id)
    return {"deleted": success}

@router.post("/upload/")
def upload_csv(file: UploadFile = File(...),
               db: Session = Depends(database.SessionLocal),
               current_user=Depends(auth.get_current_user)):
    file_path = f"./{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    data = utils.process_csv(file_path)
    for item in data:
        expense_service.create_expense(db, schemas.ExpenseCreate(**item), current_user.id)
    return {"message": f"{len(data)} expenses added successfully."}
