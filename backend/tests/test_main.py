"""
Test examples for FastAPI endpoints.
These tests show how to test your API routes using FastAPI's TestClient.
"""
import pytest
from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_read_main():
    """Test the main root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    # Check that we get a welcome message (content may vary by project)
    data = response.json()
    assert "message" in data
    assert "API" in data["message"]


def test_health_endpoint():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "timestamp" in data


def test_api_health():
    """Test the API health endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "message" in data


def test_api_example():
    """Test the API example endpoint."""
    response = client.get("/api/example")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "count" in data
    assert data["count"] == 1


def test_openapi_docs():
    """Test that OpenAPI documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200
    
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "openapi" in data
    assert "info" in data


@pytest.mark.asyncio
async def test_app_lifespan():
    """Test that the app starts and shuts down properly."""
    # This test ensures the lifespan events work correctly
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200