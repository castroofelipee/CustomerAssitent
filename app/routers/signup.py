from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import orm
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.dependencies.dependecies import get_user_service
from app.models.models import User
from app.schemas.auth_schema import TokenResponse, UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/auth")


@router.post("/signup", response_model=TokenResponse)
async def signup(
    user_create: UserCreate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
):
    return await user_service.create_user(user_create)
