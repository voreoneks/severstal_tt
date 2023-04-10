from pydantic import BaseModel
from datetime import datetime


class PictureModel(BaseModel):
    size: int
    created_at: datetime
