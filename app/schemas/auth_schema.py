from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
