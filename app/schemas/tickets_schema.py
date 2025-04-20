from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TicketBase(BaseModel):
    title: str
    description: str

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: UUID
    status: str
    created_at: datetime
    user_id: UUID
    
    class Config:
        from_attributes = True

class MessageCreate(BaseModel):
    content: str

class MessageOut(BaseModel):
    id: UUID
    content: str
    is_ai: bool
    created_at: datetime

    class Config:
        orm_mode = True

class TicketOut(BaseModel):
    id: UUID
    title: str
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

class TicketWithMessages(TicketOut):
    messages: list[MessageOut]

