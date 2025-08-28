from typing import List, Optional
from sqlmodel import Session, select
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate

def create_project(*, session: Session, project_in: ProjectCreate) -> Project:
    """
    Create a new project in the database.
    """
    # Create a Project model instance from the ProjectCreate schema
    project = Project.model_validate(project_in)

    session.add(project)
    session.commit()
    session.refresh(project)

    return project

def get_project(*, session: Session, project_id: int) -> Optional[Project]:
    """
    Retrieve a single project by its ID.
    """
    return session.get(Project, project_id)

def get_projects(*, session: Session, skip: int = 0, limit: int = 100) -> List[Project]:
    """
    Retrieve a list of projects with pagination.
    """
    statement = select(Project).offset(skip).limit(limit)
    projects = session.exec(statement).all()
    return projects

def update_project(*, session: Session, db_project: Project, project_in: ProjectUpdate) -> Project:
    """
    Update an existing project in the database.
    """
    # Get the input data as a dictionary, excluding any fields that were not set
    update_data = project_in.model_dump(exclude_unset=True)

    # Update the database project instance with the new data
    for key, value in update_data.items():
        setattr(db_project, key, value)

    session.add(db_project)
    session.commit()
    session.refresh(db_project)

    return db_project

def delete_project(*, session: Session, project_id: int) -> Optional[Project]:
    """
    Delete a project from the database by its ID.
    """
    project = session.get(Project, project_id)
    if project:
        session.delete(project)
        session.commit()
        # After commit, the project object is expired. We can return it
        # but accessing its attributes might raise an error if not configured.
        # Returning the object is useful to confirm what was deleted.
    return project
