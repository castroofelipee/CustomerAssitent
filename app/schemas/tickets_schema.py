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
