from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from .config import auth_config
router = APIRouter()

# in production you can use Settings management
# from pydantic to get secret key from .env


class Settings(BaseModel):
    authjwt_secret_key: str = auth_config.JWT_SECRET

# callback to get your configuration


@AuthJWT.load_config
def get_config():
    return Settings()

# exception handler for authjwt
# in production, you can tweak performance using orjson response


@router.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@router.get("/")
async def api():
    """Returns data from api"""
    return {"message": "Welcome to API"}
