# backend/routes/api.py
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# Create the router
router = APIRouter()

# Example Pydantic models for request/response validation
class HealthResponse(BaseModel):
    status: str
    message: str

class ExampleResponse(BaseModel):
    data: Dict[str, Any]
    count: int

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint for the API."""
    return HealthResponse(
        status="healthy",
        message="API is running successfully"
    )

@router.get("/example", response_model=ExampleResponse)
async def get_example_data():
    """Example endpoint demonstrating proper FastAPI patterns."""
    return ExampleResponse(
        data={"sample": "data", "timestamp": "2025-01-01T00:00:00Z"},
        count=1
    )
