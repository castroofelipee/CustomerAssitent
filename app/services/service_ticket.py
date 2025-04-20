from typing import List
from app.models.models import Ticket, User
from app.schemas.tickets_schema import TicketCreate

class TicketService:
    def __init__(self, db):
        self.db = db

    def get_tickets(self, user: User) -> List[Ticket]:
        return user.tickets

    def create_ticket(self, user: User, ticket_data: TicketCreate) -> Ticket:
        ticket = Ticket(
            title=ticket_data.title,
            description=ticket_data.description,
            user_id=user.id
        )
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
