from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.db.session import create_db_and_tables
from app.api.v1.api import api_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager to handle application startup and shutdown events.
    """
    # On startup, create the database and tables if they don't exist.
    print("Application startup: creating database and tables...")
    create_db_and_tables()
    yield
    # On shutdown
    print("Application shutdown.")

# Create the FastAPI app instance
app = FastAPI(
    title="Portfolio CMS API",
    description="API for managing portfolio content.",
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for health checks.
    """
    return {"message": "Welcome to the Portfolio CMS API"}

# Include the API router from v1, prefixing all routes with /api/v1
app.include_router(api_router, prefix="/api/v1")
