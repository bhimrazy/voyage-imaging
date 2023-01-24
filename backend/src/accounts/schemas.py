import uuid
from .models import User
from .security import hash_password, check_password
from pydantic import BaseModel, validator, EmailStr


class UserCreate(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    full_name: str
    email: EmailStr
    password: str
    is_admin: bool = False
    is_active: bool = True

    def hash_password(self) -> None:
        self.password = hash_password(self.password)

    def to_orm(self):
        return User(**self.dict())


class UserResponse(BaseModel):
    id: uuid.UUID
    full_name: str
    email: EmailStr
    is_admin: bool


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    def check_password(self, password_in_db) -> bool:
        return check_password(self.password, password_in_db)
