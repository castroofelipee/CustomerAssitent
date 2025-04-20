import pytest
from app.models.models import User

def test_signup_success(client, db_session):
    payload = {
        "email": "user@example.com",
        "password": "supersecure123"
    }

    response = client.post("/auth/signup", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == payload["email"]
    assert "id" in data

    db_user = db_session.query(User).filter_by(email=payload["email"]).first()
    assert db_user is not None
    assert db_user.hashed_password != payload["password"]
    assert db_user.hashed_password.startswith("$2b$")

def test_signup_email_already_exists(client, db_session):
    payload = {
        "email": "user@example.com",
        "password": "anotherpass"
    }

    response = client.post("/auth/signup", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

