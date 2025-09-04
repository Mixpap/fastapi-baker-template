# backend/main.py
from typing import Dict, Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from datetime import datetime
from loguru import logger

# Import the router from your routes module
from .routes import api

logger.add(
    level="DEBUG", sink="backend/logs/app.log", rotation="1 MB"
)  # Automatically rotate too big file

# Lifespan context manager for managing resources
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on application startup
    logger.info("Application startup...")
    
    yield  # Application runs after this yield
    
    # Code to run on application shutdown
    logger.info("Application shutdown...")

# Create the FastAPI application instance
app = FastAPI(
    title="{{project_name}} API",
    description="API for {{project_name}}",
    version="0.1.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:5173",
        "http://0.0.0.0:3000",  # Docker frontend address
        "http://0.0.0.0:8000",  # Docker backend address
        "http://frontend:3000",  # Docker service name
        "http://backend:8000",  # Docker service name
        "null",  # Allow file:// protocol for local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional: Example of accessing settings on startup (be careful with printing secrets)
# @app.on_event("startup")
# async def on_startup():
#     settings = get_settings()
#     print(f"FastAPI application starting up...")
#     print(f"Attempting to use Azure Storage Account: {settings.AZURE_STORAGE_ACCOUNT_NAME}")
# DO NOT print AZURE_SAS_TOKEN or other sensitive info in production logs.

# Include routers
app.include_router(
    api.router,
    prefix="/api",
    tags=["API"],
)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}


