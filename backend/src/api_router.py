from fastapi import APIRouter
from src.accounts import router as accounts
from src.patients import router as patients

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(accounts.router)
router.include_router(patients.router)


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}
