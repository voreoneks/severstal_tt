from sqlalchemy import (
    Column,
    Integer,
    Table,
    TIMESTAMP,
)

from app.db.tables import metadata


pictures_table = Table(
    "pictures_table",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("size", Integer, nullable=False),
    Column("created_at", TIMESTAMP(), nullable=False)
)
