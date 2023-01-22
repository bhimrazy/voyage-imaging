from typing import Any
from pydantic import BaseSettings, PostgresDsn



class Settings(BaseSettings):
    """ Application configuration."""
    DATABASE_URL: PostgresDsn

    SITE_DOMAIN: str = "myapp.com"

    app_name: str = "Awesome API"

    class Config:
        """Pydantic config."""
        env_file = ".env"


settings = Settings()
