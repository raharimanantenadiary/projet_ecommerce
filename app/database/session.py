from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.core.config import config

moteur_async = create_async_engine(
    config.url_bdd_async,
    echo=False,
    pool_pre_ping=True,
)

FabriqueSessionAsync = async_sessionmaker(
    bind=moteur_async,
    class_=AsyncSession,
    expire_on_commit=False,
)
