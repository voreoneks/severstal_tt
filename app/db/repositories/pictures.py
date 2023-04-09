from app.db.repositories.base import BaseRepository
from app.models.pictures import PictureModel
from app.db.tables.pictures import pictures_table


class PicturesRepository(BaseRepository):
    model = PictureModel
    table = pictures_table

    async def create(self, data: model):
        async with self.session.begin() as session:
            q = self.table.insert().values(**data.dict())
            await session.execute(q)

    async def delete_all(self):
        async with self.session.begin() as session:
            q = self.table.delete()
            await session.execute(q)
