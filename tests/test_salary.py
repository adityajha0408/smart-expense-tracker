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


def test_set_salary(token):
    headers = {"Authorization": f"Bearer {token}"}
    salary = {"monthly_salary": 5000.0}
    response = client.post("/salary/", json=salary, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["monthly_salary"] == 5000.0

def test_optimize_salary(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/salary/optimize/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "total_salary" in data
    assert "suggestions" in data
