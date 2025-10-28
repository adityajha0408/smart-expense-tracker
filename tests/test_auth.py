def test_register_user(user_data):
    response = client.post("/auth/register", json=user_data)
    assert response.status_code in [200, 400]  # 400 if already exists

def test_login_user(user_data):
    response = client.post("/auth/login", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
