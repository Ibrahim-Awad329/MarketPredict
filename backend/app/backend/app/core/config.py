from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    celery_broker_url: str
    celery_result_backend: str
    secret_key: str
    proxy_api_key: str = ""
    twocaptcha_api_key: str = ""
    model_path: str
    scaler_path: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
