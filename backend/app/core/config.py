"""Application configuration settings"""
from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    """Application settings from environment variables"""
    # Database
    database_url: str = "postgresql://postgres:postgres@db:5432/marketpredict"
    postgres_password: str = "postgres"
    
    # Redis
    redis_url: str = "redis://redis:6379/0"
    
    # Celery
    celery_broker_url: str = "redis://redis:6379/0"
    celery_result_backend: str = "redis://redis:6379/1"
    
    # Security
    secret_key: str = "super_secret_key_change_me_in_production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # API Keys
    proxy_api_key: str = ""
    twocaptcha_api_key: str = ""
    
    # ML Models
    model_path: str = "/app/models/lstm_model.joblib"
    scaler_path: str = "/app/models/scaler.joblib"
    
    # App Settings
    app_name: str = "MarketPredict API"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
