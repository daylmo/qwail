"""`config.py` - Core config module."""

from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Setup environment variables or read from a dotenv file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    PROJECT_NAME: str
    DEBUG: bool = False  # XXX: Definitely set this to False in production.

    # Database setup
    # For `sqlite` compatibility in development `None` values are allowed.
    # But in production use some other RDBMS like `Postgresql` or `MySQL`.
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_HOST: str = ""
    DB_PORT: int | None = None
    DB_SCHEME: str = "sqlite"
    DB_NAME: str = "qwail.sqlite3"

    @property
    def DATABASE_URL(self) -> MultiHostUrl:
        """Construct `DATABASE_URL` from database constraints."""
        return MultiHostUrl.build(
            scheme=self.DB_SCHEME,
            username=self.DB_USER,
            password=self.DB_PASS,
            host=self.DB_HOST,
            port=self.DB_PORT,
            path=self.DB_NAME,
        )


settings = Settings()
