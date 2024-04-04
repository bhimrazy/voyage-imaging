from typing import Dict

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from src.ml_model.predict import get_result

# Define application
app = FastAPI(
    title="Voyage Imaging app",
    description="Voyage Imaging app!",
    version="0.1",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    """Return a welcome message."""
    return {"message": "Welcome to Voyage Imaging app!"}


@app.post("/api/v1/predict")
async def predict(file: UploadFile = File(...)):
    return get_result(image_file=file, is_api=True)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> Dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)