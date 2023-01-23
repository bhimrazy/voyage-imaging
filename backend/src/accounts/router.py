import uuid

from fastapi import APIRouter, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from .config import auth_config
from pydantic import BaseModel

from .models import User
from src.database import database
from sqlalchemy import insert, select
from .schemas import UserCreate, UserResponse, UserLogin

router = APIRouter()

# in production you can use Settings management
# from pydantic to get secret key from .env


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


def hash_password(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw, salt)


def check_password(password: str, password_in_db: bytes) -> bool:
    password_bytes = bytes(password, "utf-8")
    return bcrypt.checkpw(password_bytes, password_in_db)


@router.post('/token')
async def login(user: UserLogin, Authorize: AuthJWT = Depends()):
    query = User.__table__.select().where(User.email == user.email)
    existing_user = await database.fetch_one(query)
    if not existing_user:
        raise HTTPException(status_code=400, detail="Email does not exist.")

    print("password", user.check_password(existing_user.password))
    if not user.check_password(existing_user.password):
        raise HTTPException(status_code=400, detail="Password mismatch.")

    access_token = Authorize.create_access_token(subject=user.email)
    return {"access_token": access_token}


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
