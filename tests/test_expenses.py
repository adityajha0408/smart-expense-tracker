import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def token():
    login_data = {"username": "testuser", "password": "testpass123"}
    response = client.post("/auth/login", json=login_data)  # <-- use json= instead of data=
    data = response.json()
    return data["access_token"]


def test_add_expense(token):
    headers = {"Authorization": f"Bearer {token}"}
    expense = {"description": "Grocery shopping", "amount": 50.0, "category": "food"}
    response = client.post("/expenses/", json=expense, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Grocery shopping"
    assert data["amount"] == 50.0

def test_list_expenses(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/expenses/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
