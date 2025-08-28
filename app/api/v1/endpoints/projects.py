from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app import crud
from app.db.session import get_session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate
from app.dependencies import get_current_user_placeholder

router = APIRouter()

@router.get("/", response_model=List[ProjectRead])
def read_projects(
    *,
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100
) -> List[Project]:
    """
    Retrieve all projects with pagination. This is a public endpoint.
    """
    projects = crud.get_projects(session=session, skip=skip, limit=limit)
    return projects

@router.get("/{project_id}", response_model=ProjectRead)
def read_project(
    *,
    session: Session = Depends(get_session),
    project_id: int
) -> Project:
    """
    Retrieve a single project by its ID. This is a public endpoint.
    """
    project = crud.get_project(session=session, project_id=project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )
    return project

@router.post("/", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    *,
    session: Session = Depends(get_session),
    project_in: ProjectCreate,
    current_user: Any = Depends(get_current_user_placeholder)
) -> Project:
    """
    Create a new project. This is a protected endpoint.
    Requires a valid JWT token.
    """
    project = crud.create_project(session=session, project_in=project_in)
    return project

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(
    *,
    session: Session = Depends(get_session),
    project_id: int,
    project_in: ProjectUpdate,
    current_user: Any = Depends(get_current_user_placeholder)
) -> Project:
    """
    Update an existing project. This is a protected endpoint.
    Requires a valid JWT token.
    """
    db_project = crud.get_project(session=session, project_id=project_id)
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )
    project = crud.update_project(session=session, db_project=db_project, project_in=project_in)
    return project

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    *,
    session: Session = Depends(get_session),
    project_id: int,
    current_user: Any = Depends(get_current_user_placeholder)
) -> None:
    """
    Delete a project by its ID. This is a protected endpoint.
    Requires a valid JWT token.
    """
    project = crud.delete_project(session=session, project_id=project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found",
        )
    return None
