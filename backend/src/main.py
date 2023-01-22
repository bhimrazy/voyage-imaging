from fastapi import FastAPI
from .database import database
from typing import *

app = FastAPI()


@app.get("/")
def index():
    """Return a welcome message."""
    return {"message": "Welcome to Voyage Imaging app!"}


@app.on_event("startup")
async def startup() -> None:
    """Connect to the database on startup."""

    await database.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Disconnect from the database on shutdown."""
    await database.disconnect()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> Dict[str, str]:
    return {"status": "ok"}
