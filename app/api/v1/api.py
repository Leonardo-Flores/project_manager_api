from fastapi import APIRouter
from app.api.v1.endpoints import projects

api_router = APIRouter()

# Include the projects router with a prefix and tags
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])

# Other routers for v1 of the API can be added here
# For example:
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
