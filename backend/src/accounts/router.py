import uuid
import json
from fastapi import APIRouter, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from .config import auth_config
from pydantic import BaseModel

from .models import User
from src.database import database
from .schemas import UserCreate, UserResponse, UserLogin
router = APIRouter()

# in production you can use Settings management
# from pydantic to get secret key from .env


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/token')
async def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    query = User.__table__.select().where(User.email == user.email)
    existing_user = await database.fetch_one(query)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Email does not exist.")

    if not user.check_password(existing_user.password):
        raise HTTPException(status_code=400, detail="Password mismatch.")

    data = {
        "id": str(existing_user.id),
        "email": existing_user.email,
        "is_admin": existing_user.is_admin,
    }
    access_token = Authorize.create_access_token(subject=json.dumps(data))
    return {"access_token": access_token}


@router.get('/users/me')
def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": json.loads(current_user)}


@router.post("/users/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserCreate):

    query = User.__table__.select().where(User.email == user.email)
    existing_user = await database.fetch_one(query)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.hash_password()
    query = User.__table__.insert().values(**user.dict()).returning(User)
    data = await database.fetch_one(query)
    return {
        "id": data.id,
        "full_name": data.full_name,
        "email": data.email,
        "is_admin": data.is_admin,
    }
