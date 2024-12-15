from pydantic import BaseSettings
from pathlib import Path

from functools import lru_cache
import os


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    SLACK_WEBHOOK_URL: str
    SLACK_BOT_TOKEN: str

    class Config:
        env_file = str(BASE_DIR / ".env")
        env_file_encoding = "utf-8"


class TestSettings(BaseSettings):
    SLACK_WEBHOOK_URL: str
    SLACK_BOT_TOKEN: str

    class Config:
        env_file = str(BASE_DIR / ".env")
        env_file_encoding = "utf-8"


@lru_cache
def get_settings():
    if os.getenv("APP_ENV", "DEVELOP") == "TEST":
        return TestSettings()
    return Settings()


settings = get_settings()
