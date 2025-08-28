from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application settings are loaded from environment variables.
    A .env file can be used for local development.
    """
    DATABASE_URL: str = "postgresql://user:password@localhost/db"

    # The model_config attribute replaces the Config class in Pydantic v2
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')

settings = Settings()
