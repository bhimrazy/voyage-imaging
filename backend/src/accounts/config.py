from pydantic import BaseSettings


class AuthConfig(BaseSettings):
    JWT_ALG: str
    JWT_SECRET: str
    JWT_EXP: int = 5  # minutes

    class Config:
        """Pydantic config."""
        env_file = ".env"


auth_config = AuthConfig()
