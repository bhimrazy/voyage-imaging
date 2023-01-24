import uuid
from .models import Patient
from pydantic import BaseModel, validator, EmailStr


class PatientCreate(BaseModel):
    id: uuid.UUID = None
    name: str
    age: int
    gender: str = "male"
    phone: str
    address: str
    doctor_id: uuid.UUID = None


class PatientResponse(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    age: int
    gender: str = "male"
    phone: str
    address: str
    doctor_id: uuid.UUID = None
