from fastapi import FastAPI
from routers import reservations

app = FastAPI(title="Morning Huddle API")

app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])

