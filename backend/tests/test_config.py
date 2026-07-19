"""Tests for configuration"""
import pytest
from app.core.config import get_settings, Settings

def test_settings_singleton():
    """Test that settings is a singleton"""
    settings1 = get_settings()
    settings2 = get_settings()
    assert settings1 is settings2

def test_settings_defaults():
    """Test default settings values"""
    settings = get_settings()
    assert settings.app_name == "MarketPredict API"
    assert settings.algorithm == "HS256"
    assert settings.access_token_expire_minutes == 30
