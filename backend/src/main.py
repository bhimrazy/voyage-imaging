from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from .database import database
from typing import *

from .api_router import router

# Define application
app = FastAPI(
    title="Voyage Imaging app",
    description="Voyage Imaging app!",
    version="0.1",
)

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
