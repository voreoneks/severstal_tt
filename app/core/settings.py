from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: True

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
