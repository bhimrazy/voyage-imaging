import uuid
import json
from fastapi import APIRouter, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from typing import *
from pydantic import BaseModel

from .models import Patient
from src.database import database
from .schemas import PatientCreate, PatientResponse
router = APIRouter()

@router.get("/patients/", status_code=status.HTTP_200_OK, response_model=List[PatientResponse])
async def get_patients(Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    query = Patient.__table__.select().where(Patient.doctor_id == user["id"])
    datas = await database.fetch_all(query)

    return PatientResponse.parse(datas)


@router.get("/patients/{patient_id}", status_code=status.HTTP_200_OK, response_model=PatientResponse)
async def get_patients(patient_id:str ,Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())
    try:
        query = Patient.__table__.select().where(Patient.id == patient_id)
        patient = await database.fetch_one(query)
    except Exception as e: 
        raise HTTPException(status_code=404, detail=e.message)

    return PatientResponse.parse(patient)


@router.post("/patients/", status_code=status.HTTP_201_CREATED, response_model=PatientResponse)
async def create_patient(patient: PatientCreate, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    patient.id = uuid.uuid4()
    patient.doctor_id = user["id"]
    query = Patient.__table__.insert().values(**patient.dict()).returning(Patient)
    data = await database.fetch_one(query)
    return {
        "id": data.id,
        "name": data.name,
        "age": data.age,
        "gender": data.gender,
        "phone": data.phone,
        "address": data.address,
        "doctor_id": data.doctor_id,
    }
