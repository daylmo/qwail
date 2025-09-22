from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

from qwail.core.config import settings

engine = create_async_engine(
    url=str(settings.DATABASE_URL),
    poolclass=NullPool,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)


class DBase(AsyncAttrs, DeclarativeBase):
    pass
