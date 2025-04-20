from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app.database.db import init_db
from app.routers import login, signup


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.middleware("http")
async def set_secure_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


app.include_router(signup.router)
app.include_router(login.router)
