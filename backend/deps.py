# backend/deps.py
"""
Dependency injection module for FastAPI application.
Contains shared dependencies like settings and authentication.
"""

from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import logging

def get_logger() -> logging.Logger:
    """Returns the 'app' logger instance."""
    return logging.getLogger("app")

class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    
    # Basic app settings
    app_name: str = Field(default="FastAPI Application", env="APP_NAME")

@lru_cache()
def get_settings() -> Settings:
    """
    Create settings instance with caching.
    This ensures settings are loaded only once.
    """
    return Settings()

# Dependency to get settings in route handlers
SettingsDep = Annotated[Settings, Depends(get_settings)]
