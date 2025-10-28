# Smart Expense Tracker

Smart Expense Tracker is a **FastAPI-based backend application** to manage expenses, track salaries, and optimize salary expenditure. It features user authentication, expense management, and salary optimization tools.

---

## Features

- **User Authentication** (Register/Login)
- **Expense Management** (Add, List, Delete)
- **Salary Management** (Set Salary, Optimize Expenditure)
- **JWT-based authentication**
- **Optimized and modular FastAPI backend**

---

## Project Structure

```

smart_expense_tracker/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── expenses.py
│   │   └── salary.py
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── expense_service.py
│   │   └── salary_service.py
│   ├── config.py
│   └── auth.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_expenses.py
│   └── test_salary.py
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/PrasunK8/smart_expense_tracker.git
cd smart_expense_tracker
````

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Create a `.env` file** in the root directory and add:

```env
DATABASE_URL=sqlite:///./expense_tracker.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Running the Project

```bash
uvicorn app.main:app --reload
```

* Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the **Swagger UI** and test the API.

---

## Running Tests

```bash
pytest tests/ --disable-warnings -v
```

---

## Usage

1. **Register a new user** via `/auth/register`.
2. **Login** via `/auth/login` to get the JWT token.
3. **Use the token** in the Authorization header (`Bearer <token>`) for all other endpoints.
4. **Add Expenses**, **View Expenses**, and **Set/Optimize Salary** using the respective endpoints.

---

## License

This project is **MIT Licensed**.

```

