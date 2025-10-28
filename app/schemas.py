from pydantic import BaseModel
from datetime import date
from typing import Optional

# ---------- AUTH ----------
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# ---------- EXPENSE ----------
class ExpenseBase(BaseModel):
    description: str
    amount: float
    category: Optional[str] = None
    date: Optional[date] = None

class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    class Config:
        orm_mode = True

# ---------- SALARY ----------
class SalaryBase(BaseModel):
    monthly_salary: float
