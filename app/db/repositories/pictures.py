from app.db.repositories.base import BaseRepository
from app.models.pictures import PictureModel
from app.db.tables.pictures import pictures_table


class PicturesRepository(BaseRepository):
    model = PictureModel
    table = pictures_table

    async def create(self, data: model):
        q = self.table.insert().values(**data.dict())
        await self.session.execute(q)