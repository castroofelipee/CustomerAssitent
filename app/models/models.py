import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="user", nullable=False)

    tickets = relationship(
        "Ticket", back_populates="user", cascade="all, delete-orphan"
    )


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    status = Column(String(50), default="open", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="tickets")
    messages = relationship(
        "Message", back_populates="ticket", cascade="all, delete-orphan"
    )


class Message(Base):
    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = Column(String, nullable=False)
    is_ai = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    ticket_id = Column(UUID(as_uuid=True), ForeignKey("tickets.id"), nullable=False)
    ticket = relationship("Ticket", back_populates="messages")
