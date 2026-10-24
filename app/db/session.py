from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import  declarative_base

from app.core.config import settings

async_engine = create_async_engine(settings.database_url,
                                   echo=False,
                                   pool_size=10,
                                   max_overflow=10,
                                   pool_pre_ping=True,
                                   pool_recycle=3600,
                                   pool_timeout=30,)

AsyncSessionLocal = async_sessionmaker(async_engine,
                                       expire_on_commit=False,
                                       autocommit=False,
                                       autoflush=False,
                                       class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session