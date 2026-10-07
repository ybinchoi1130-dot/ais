# config.py
# pip install pydantic-settings

from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    GOOGLE_API_KEY: str
    HUGGINGFACEHUB_API_TOKEN: str = ""
    DATABASE_URL: str
    ENV: str = "development"
    DEBUG: bool = False

    # .env 파일 경로 및 인코딩 지정
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    """설정 객체를 캐싱하여 매번 파일을 읽지 않도록 함"""
    return Settings()

settings = get_settings()