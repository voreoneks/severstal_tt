from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool
    REDIS_PASS: str
    PICTURES_FOLDER: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
