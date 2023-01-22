# Databse config to conntect to the postgres database using sqlalchemy
from .config import settings
from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base()


DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)
