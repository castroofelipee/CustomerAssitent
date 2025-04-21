from pydantic import BaseModel
from typing import Optional

class Reservation(BaseModel):
    id: int
    name: str
    time: str
    party_size: int
    vip: bool
    allergies: Optional[str] = None
    special_request: Optional[str] = None
    occasion: Optional[str] = None

