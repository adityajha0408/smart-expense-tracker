import pandas as pd
from sqlalchemy.orm import Session
from .models import Expense, UserSalary

def analyze_expenses(db: Session):
    expenses = db.query(Expense).all()
    salary_record = db.query(UserSalary).first()

    if not salary_record:
        return {"message": "Set your monthly salary first."}

    salary = salary_record.monthly_salary
    df = pd.DataFrame([{"category": e.category, "amount": e.amount} for e in expenses])

    if df.empty:
        return {"message": "No expenses recorded."}

    summary = df.groupby("category").sum().reset_index()
    total_spent = df["amount"].sum()
    remaining = salary - total_spent
    percent_spent = round((total_spent / salary) * 100, 2)

    suggestions = []
    for _, row in summary.iterrows():
        if row["amount"] > 0.3 * salary:
            suggestions.append(f"Reduce spending on {row['category']} (currently {row['amount']:.2f}).")

    if remaining < 0:
        suggestions.append("You are overspending your salary. Cut expenses immediately.")
    elif remaining < 0.1 * salary:
        suggestions.append("Try saving at least 10% of your income next month.")

    return {
        "total_salary": salary,
        "total_spent": total_spent,
        "remaining": remaining,
        "percent_spent": percent_spent,
        "category_breakdown": summary.to_dict(orient="records"),
        "suggestions": suggestions
    }
