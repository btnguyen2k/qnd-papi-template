
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # DATABASE_URL: str
    # SECRET_KEY: str
    # DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
