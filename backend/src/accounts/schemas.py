from pydantic import BaseModel, validator, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str


class UserResponse(BaseModel):
    full_name: str
    email: EmailStr
