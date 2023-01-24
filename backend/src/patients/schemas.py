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
    id: uuid.UUID
    name: str
    age: int
    gender: str
    phone: str
    address: str
    doctor_id: uuid.UUID


    @staticmethod
    def parse(data):
        """parses data"""
        def parse_one(data):
            return PatientResponse(**{
                    "id": data.id,
                    "name": data.name,
                    "age": data.age,
                    "gender": data.gender,
                    "phone": data.phone,
                    "address": data.address,
                    "doctor_id": data.doctor_id,
                })
        if isinstance(data, list):
            return [parse_one(item) for item in data]
        return parse_one(data)

