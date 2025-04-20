import pytest
from app.models.models import User
from app.services.user_service import pwd_context

@pytest.fixture
def test_user(db_session):
    existing_user = db_session.query(User).filter(User.email == "testuser@example.com").first()
    if existing_user is None:
        user = User(
            email="testuser@example.com",
            hashed_password=pwd_context.hash("testpassword123")
        )
        db_session.add(user)
        db_session.commit()
        return user
    return existing_user

def test_login_success(client, test_user):
    response = client.post("/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpassword123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_credentions(client, test_user):
    response = client.post("/auth/login", json={
        "email": "test_user1@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"

def test_login_nonexistent_email(client):
    response = client.post("/auth/login", json={
        "email": "notfound@example.com",
        "password": "irrelevant"
    })
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"

