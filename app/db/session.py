from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .base import Base
from core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session