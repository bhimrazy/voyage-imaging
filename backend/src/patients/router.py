import uuid
import json
from fastapi import APIRouter, HTTPException, Depends, Request, Response, status
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from typing import *
from pydantic import BaseModel

from .models import patients, Patient, records, PatientRecord
from src.database import database
from .schemas import PatientCreate, PatientResponse, PatientRecordCreate, PatientRecordResponse
router = APIRouter()


@router.get("/patients/", status_code=status.HTTP_200_OK, response_model=List[PatientResponse])
async def get_patients(Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    query = patients.select().where(Patient.doctor_id == user["id"])
    datas = await database.fetch_all(query)

    return PatientResponse.parse(datas)


@router.get("/patients/{patient_id}", status_code=status.HTTP_200_OK, response_model=PatientResponse)
async def get_patients(patient_id: str , Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())
    try:
        query = patients.select().where(Patient.id == patient_id)
        patient = await database.fetch_one(query)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.message)

    if not patient:

        raise HTTPException(
            status_code=404, detail=f"Patient with {patient_id} not found")
    return PatientResponse.parse(patient)


@router.post("/patients/", status_code=status.HTTP_201_CREATED, response_model=PatientResponse)
async def create_patient(patient: PatientCreate, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    patient.id = uuid.uuid4()
    patient.doctor_id = user["id"]
    query = patients.insert().values(**patient.dict()).returning(patients)
    data = await database.fetch_one(query)
    return PatientResponse.parse(data)


@router.get("/patient/{patient_id}/records", status_code=status.HTTP_200_OK, response_model=List[PatientRecordResponse])
async def get_patient_records(patient_id: str, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    try:
        query = records.select().where(PatientRecord.patient_id == patient_id)
        datas = await database.fetch_all(query)
        return PatientRecordResponse.parse(datas)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.get("/patient/{patient_id}/records/{record_id}", status_code=status.HTTP_200_OK, response_model=PatientRecordResponse)
async def get_patient_records(patient_id: str, record_id: str, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())

    try:
        query = records.select().where(PatientRecord.patient_id
                                       == patient_id, PatientRecord.id == record_id)
        record = await database.fetch_one(query)
        return PatientRecordResponse.parse(record)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.message)


@router.post("/patient/{patient_id}/records", status_code=status.HTTP_200_OK, response_model=PatientRecordResponse)
async def create_patient(patient_id: str, patient_record: PatientRecordCreate, Authorize: AuthJWT = Depends()):

    Authorize.jwt_required()
    user = json.loads(Authorize.get_jwt_subject())
    try:
        patient_record.id = uuid.uuid4()
        patient_record.patient_id = patient_id
        query = records.insert().values(**patient_record.dict()).returning(records)
        data = await database.fetch_one(query)
        return PatientRecordResponse.parse(data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e.message)
