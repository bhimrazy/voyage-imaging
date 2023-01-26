from fastapi import APIRouter, File, UploadFile
from src.accounts import router as accounts
from src.patients import router as patients
from src.ml_model.predict import get_result

router = APIRouter(prefix="/api/v1", tags=["api"])

router.include_router(accounts.router)
router.include_router(patients.router)


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    return get_result(image_file=file, is_api=True)
