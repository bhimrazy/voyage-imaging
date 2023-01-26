from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import TIMESTAMP
from src.database import Base
import uuid


class Patient(Base):
    __tablename__ = "patients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(ENUM('male', 'female', 'other',
                    name='gender_types'), nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=True)
    doctor_id = Column(UUID(as_uuid=True),
                       ForeignKey("users.id"), nullable=False)
    doctor = relationship("User", back_populates="patients")
    records = relationship("PatientRecord", back_populates="patient")

    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)


class PatientRecord(Base):
    __tablename__ = "patient_records"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column(UUID(as_uuid=True),
                        ForeignKey("patients.id"), nullable=False)
    date = Column(DateTime, default=func.now(), nullable=False)
    checkup_data = Column(Text, nullable=True)
    condition = Column(Text, nullable=True)
    patient = relationship("Patient", back_populates="records")
    image_path = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True),
                        server_default=func.now(), nullable=False)


patients = Patient.__table__
records = PatientRecord.__table__
