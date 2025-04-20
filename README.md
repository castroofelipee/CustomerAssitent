# Backend Engineering Customer Assistant
This project is a solution to the Customer Support Assistant Backend Assessment. It simulates the backend of a customer support system that allows users to create support tickets and receive AI-generated assistance using Groq's API. It emphasizes clean architecture, OOP principles, and integration with external services like PostgreSQL and Groq.

## Tech Stack
- FastAPI – High-performance Python web framework
- PostgreSQL – Relational database
- SQLAlchemy – ORM for database models
- Alembic – Database migrations
- JWT – Token-based authentication
- aiohttp – Async HTTP requests (for Groq API)
- Docker & Docker Compose – Containerization
- Groq API – AI assistant integration

## Architecture & Design

The codebase follows a **service-oriented architecture**, emphasizing **separation of concerns**, **testability**, and **clean design**.

Each layer (routers, services, repositories) is focused on a specific responsibility, making the codebase easy to navigate, extend, and test.

---

## Key Concepts Applied

| Principle / Pattern       | Applied How                                                                 |
|-----------------------------|-------------------------------------------------------------------------------|
| **OOP**                     | Modular services for auth, ticket handling, and AI logic                      |
| **Dependency Injection**    | Services injected using `FastAPI`'s `Depends()`                              |
| **Repository Pattern**      | Abstracts database operations, improving maintainability and test coverage   |
| **Factory Pattern**         | Used to dynamically generate AI prompt templates                             |
| **Encapsulation**           | Business logic is hidden inside services rather than routes                   |
| **Single Responsibility**   | Each class/module is focused on one clear task or concern                    |

---

## Example: Dependency Injection in Action

```python
@router.post("/tickets")
def create_ticket(
    request: TicketCreateRequest,
    ticket_service: TicketService = Depends(get_ticket_service)
):
    return ticket_service.create_ticket(request)

