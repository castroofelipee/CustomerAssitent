from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import orm
from sqlalchemy.orm import Session

from app.models.models import User
from app.schemas.auth_schema import UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/auth")

@router.post("/signup")
async def signup(user_create: UserCreate, user_service: UserService = Depends()):
    return await user_service.create_user(user_create)

