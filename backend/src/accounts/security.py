import json
from passlib.hash import bcrypt
from fastapi import HTTPException
from fastapi_jwt_auth import AuthJWT


def hash_password(password: str) -> bytes:
    return bcrypt.hash(password)


def check_password(password: str, password_in_db: str) -> bool:
    return bcrypt.verify(password, password_in_db)
