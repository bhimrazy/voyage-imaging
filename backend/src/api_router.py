from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["api"])


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}
