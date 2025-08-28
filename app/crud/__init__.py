from .project import (
    create_project,
    get_project,
    get_projects,
    update_project,
    delete_project,
)

# This makes the project CRUD functions available under the `crud` namespace,
# e.g., `crud.get_project`
__all__ = [
    "create_project",
    "get_project",
    "get_projects",
    "update_project",
    "delete_project",
]
