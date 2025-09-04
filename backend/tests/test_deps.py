"""
Test examples for dependency injection and settings.
These tests show how to test your dependencies and configuration.
"""
import pytest
from ..deps import get_settings, Settings


def test_get_settings():
    """Test that settings can be retrieved."""
    settings = get_settings()
    assert isinstance(settings, Settings)
    assert settings.app_name is not None


def test_settings_caching():
    """Test that settings are cached properly."""
    settings1 = get_settings()
    settings2 = get_settings()
    # Should be the same instance due to @lru_cache
    assert settings1 is settings2


def test_settings_types():
    """Test that settings have the expected types."""
    settings = get_settings()
    assert isinstance(settings.app_name, str)