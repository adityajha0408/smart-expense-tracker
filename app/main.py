from fastapi import FastAPI
from .database import Base, engine
from .models import *
from .routes import auth_routes, expense_routes, salary_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Expense Tracker API")

# Routers
app.include_router(auth_routes.router)
app.include_router(expense_routes.router)
app.include_router(salary_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Smart Expense Tracker API"}
