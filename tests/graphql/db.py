from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine =create_async_engine(
    "sqlite+aiosqlite:///./database_test.db"
)

testing_async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@asynccontextmanager
async def overide_get_session() -> AsyncGenerator[AsyncSession, None]:
    async with testing_async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()