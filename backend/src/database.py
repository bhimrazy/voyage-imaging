# Databse config to conntect to the postgres database using sqlalchemy
from .config import settings
from databases import Database

DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)
