from typing import Type
import abc

from pydantic.main import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(abc.ABC):
    def __init__(self, session: AsyncSession):
        super().__init__()
        self._session = session

    @property
    def session(self) -> AsyncSession:
        return self._session

    @staticmethod
    def _map_db_object(row, to_schema: Type[BaseModel]) -> Type[BaseModel]:
        row = dict(row)

        return to_schema(**row)
