from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core import config


DATABASE_URL = config.DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=config.DEBUG)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False, autoflush=True
)
