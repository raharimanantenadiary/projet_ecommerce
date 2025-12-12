from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import FabriqueSessionAsync

async def obtenir_db() -> AsyncGenerator[AsyncSession, None]:
    async with FabriqueSessionAsync() as session:
        yield session
