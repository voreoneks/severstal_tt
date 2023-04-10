from sqlalchemy.orm.decl_api import registry


mapper_registry = registry()
metadata = mapper_registry.metadata


def get_metadata():
    """Import all project tables"""
    from app.db.tables.pictures import pictures_table

    return mapper_registry.metadata
