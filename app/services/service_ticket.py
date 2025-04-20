from typing import List
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from app.models.models import Ticket, Message, User
from app.schemas.tickets_schema import TicketCreate, MessageCreate


class TicketService:
    @staticmethod
    async def get_user_tickets(db: AsyncSession, user: User) -> List[Ticket]:
        result = await db.execute(select(Ticket).where(Ticket.user_id == user.id))
        return result.scalars().all()

    @staticmethod
    async def create_ticket(db: AsyncSession, user: User, ticket_in: TicketCreate) -> Ticket:
        new_ticket = Ticket(
            title=ticket_in.title,
            description=ticket_in.description,
            user_id=user.id
        )
        db.add(new_ticket)
        await db.commit()
        await db.refresh(new_ticket)
        return new_ticket

    @staticmethod
    async def get_ticket_with_messages(db: AsyncSession, ticket_id: UUID, user: User) -> Ticket:
        ticket = await db.get(Ticket, ticket_id)
        if not ticket or ticket.user_id != user.id:
            raise HTTPException(status_code=404, detail="Ticket not found")
        await db.refresh(ticket)
        return ticket

    @staticmethod
    async def add_message_to_ticket(
        db: AsyncSession,
        ticket_id: UUID,
        message: MessageCreate,
        user: User
    ) -> Message:
        ticket = await db.get(Ticket, ticket_id)
        if not ticket or ticket.user_id != user.id:
            raise HTTPException(status_code=404, detail="Ticket not found")

        new_message = Message(
            content=message.content,
            ticket_id=ticket_id,
            is_ai=False
        )
        db.add(new_message)
        await db.commit()
        await db.refresh(new_message)
        return new_message

