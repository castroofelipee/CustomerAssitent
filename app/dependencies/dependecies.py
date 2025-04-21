from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.services.user_service import AuthService, UserService


def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)


def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)
