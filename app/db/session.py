from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# The database URL is taken from the settings
# echo=True will log all SQL statements, which is useful for debugging.
engine = create_engine(settings.DATABASE_URL, echo=True)

def get_session():
    """
    Dependency to get a database session.
    This will be used in the API endpoints.
    """
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    """
    Creates all tables in the database based on SQLModel metadata.
    This should be called once on application startup.
    """
    SQLModel.metadata.create_all(engine)
