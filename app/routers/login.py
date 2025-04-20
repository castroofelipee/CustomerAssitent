from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.auth_schema import UserLogin
from app.services.user_service import AuthService

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
    auth_service: AuthService = Depends(),
):
    try:
        user = await auth_service.authenticate_user(
            db, credentials.email, credentials.password
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return {"access_token": "token", "token_type": "bearer"}
