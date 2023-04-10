from typing import Type
import abc

from pydantic.main import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.setup import async_session


class BaseRepository(abc.ABC):
    def __init__(self):
        super().__init__()
        self._session: AsyncSession = async_session

    @property
    def session(self) -> AsyncSession:
        return self._session

    @staticmethod
    def _map_db_object(row, to_schema: Type[BaseModel]) -> Type[BaseModel]:
        row = dict(row)

        return to_schema(**row)
