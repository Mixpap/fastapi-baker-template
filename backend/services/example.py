# backend/services/example.py
"""Example service with simple business logic."""

import logging
from datetime import datetime
from typing import Dict, Any

logger = logging.getLogger(__name__)

async def get_example_data() -> Dict[str, Any]:
    """
    Example service function.
    Keep business logic simple and focused.
    """
    logger.info("Fetching example data")
    
    return {
        "message": "Hello from service layer",
        "timestamp": datetime.now().isoformat(),
        "data": {"key": "value"}
    }

async def process_user_data(user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Example of processing user data.
    This is where you'd put actual business logic.
    """
    logger.info(f"Processing data for user: {user_id}")
    
    # Your business logic here
    processed_data = {
        "user_id": user_id,
        "processed_at": datetime.now().isoformat(),
        "result": f"Processed {len(data)} items"
    }
    
    return processed_data
