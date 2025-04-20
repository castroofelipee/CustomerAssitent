import pytest
from unittest import mock
from app.models.models import Ticket, User
from app.schemas.tickets_schema import TicketCreate
from app.services.service_ticket import TicketService

@pytest.fixture
def mock_db():
    mock_db = mock.MagicMock()
    return mock_db

@pytest.fixture
def mock_user():
    user = mock.MagicMock(spec=User)
    user.id = 1
    user.tickets = [
        Ticket(id=1, title="Ticket 1", description="Description 1", user_id=1),
        Ticket(id=2, title="Ticket 2", description="Description 2", user_id=1)
    ]
    return user

@pytest.fixture
def mock_ticket_data():
    return TicketCreate(title="New Ticket", description="New Ticket Description")

@pytest.fixture
def ticket_service(mock_db):
    return TicketService(db=mock_db)

def test_get_tickets(ticket_service, mock_user):
    tickets = ticket_service.get_tickets(mock_user)
    assert len(tickets) == 2
    assert tickets[0].title == "Ticket 1"
    assert tickets[1].title == "Ticket 2"

def test_create_ticket(ticket_service, mock_db, mock_user, mock_ticket_data):
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None

    created_ticket = ticket_service.create_ticket(mock_user, mock_ticket_data)

    mock_db.add.assert_called_once()
    added_ticket = mock_db.add.call_args[0][0]

    assert isinstance(added_ticket, Ticket)
    assert added_ticket.title == "New Ticket"
    assert added_ticket.description == "New Ticket Description"
    assert added_ticket.user_id == mock_user.id

    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()
    refreshed_ticket = mock_db.refresh.call_args[0][0]

    assert refreshed_ticket == added_ticket

    assert created_ticket.title == "New Ticket"
    assert created_ticket.description == "New Ticket Description"
    assert created_ticket.user_id == mock_user.id

