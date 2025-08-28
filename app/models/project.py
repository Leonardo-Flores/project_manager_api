import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, JSON, Column
from sqlalchemy import func

class Project(SQLModel, table=True):
    """
    Represents a project in the portfolio.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    detailed_content: str
    github_link: Optional[str] = None
    project_link: Optional[str] = None

    # Store a list of strings as JSON in the database
    technologies: List[str] = Field(sa_column=Column(JSON))

    is_featured: bool = Field(default=False)

    # Timestamps are handled by the database for reliability
    created_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
        sa_column_kwargs={"server_default": func.now()}
    )
    updated_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()}
    )
