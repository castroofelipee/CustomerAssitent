from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session, sessionmaker

from app.models.models import User
from app.routers import ai_service
from app.schemas.tickets_schema import (
    MessageCreate,
    TicketCreate,
    TicketOut,
    TicketWithMessages,
)
from app.services import service_ticket
from app.services.user_service import get_current_user, get_db

router = APIRouter()


@router.get("/", response_model=list[TicketOut])
async def list_tickets(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return await service_ticket.get_user_tickets(db, current_user)


@router.post("/", response_model=TicketOut)
async def create_ticket(
    ticket_in: TicketCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await service_ticket.create_ticket(db, current_user, ticket_in)


@router.get("/{ticket_id}", response_model=TicketWithMessages)
async def get_ticket(
    ticket_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await service_ticket.get_ticket_with_messages(db, ticket_id, current_user)


@router.post("/{ticket_id}/messages")
async def add_message(
    ticket_id: UUID,
    message: MessageCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await service_ticket.add_message_to_ticket(
        db, ticket_id, message, current_user
    )


@router.get("/{ticket_id}/ai-response")
async def stream_ai_response(
    ticket_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    async def event_stream():
        async for chunk in ai_service.generate_response_stream(
            db, ticket_id, current_user
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
