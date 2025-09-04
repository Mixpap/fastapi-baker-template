"""
Test examples for business logic services.
These tests show how to test your service functions and business logic.
"""
import pytest
from ..services.example import get_example_data, process_user_data


@pytest.mark.asyncio
async def test_get_example_data():
    """Test the example service function."""
    result = await get_example_data()
    
    assert "message" in result
    assert "timestamp" in result
    assert "data" in result
    assert result["message"] == "Hello from service layer"


@pytest.mark.asyncio
async def test_process_user_data():
    """Test user data processing."""
    user_id = "123"
    input_data = {"item1": "value1", "item2": "value2"}
    
    result = await process_user_data(user_id, input_data)
    
    assert result["user_id"] == user_id
    assert "processed_at" in result
    assert "result" in result
    assert "2 items" in result["result"]
