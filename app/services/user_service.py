from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from app.database.db import get_db
from app.models.models import User
from app.schemas.auth_schema import UserCreate
from app.config import settings
import uuid
from datetime import timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    async def create_user(self, user_data: UserCreate):
        if self.get_user_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pw = self.hash_password(user_data.password)
        new_user = User(
            id=uuid.uuid4(),
            email=user_data.email,
            hashed_password=hashed_pw
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user


class AuthService:
    async def authenticate_user(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if user is None:
            raise ValueError("Invalid email or password")
        if not self.verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")
        return user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

