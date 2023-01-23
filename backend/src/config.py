from typing import Any
from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    """ Application configuration."""
    DATABASE_URL: PostgresDsn

    class Config:
        """Pydantic config."""
        env_file = ".env"


settings = Settings()
