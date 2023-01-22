# Databse config to conntect to the postgres database using sqlalchemy
from .config import settings
from databases import Database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = settings.DATABASE_URL

# engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# engine = create_engine(DATABASE_URL)
print(DATABASE_URL)
database = Database(DATABASE_URL)


