import aiohttp
from app.models.models import Ticket
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import User
from fastapi import HTTPException
from uuid import UUID
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def generate_response_stream(db: AsyncSession, ticket_id: UUID, user: User):
    ticket = await db.get(Ticket, ticket_id)
    if not ticket or ticket.user_id != user.id:
        raise HTTPException(status_code=404, detail="Ticket not found")

    prompt = f"""
    You are a helpful assistant.
    Ticket: {ticket.title}
    Description: {ticket.description}
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.groq.com/v1/chat/completions", json={
            "model": "mixtral-8x7b-32768",
            "stream": True,
            "messages": [{"role": "user", "content": prompt}]
        }, headers=headers) as resp:
            async for line in resp.content:
                yield line.decode("utf-8")

