from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool, create_engine
from src.repositories.models import Base
from alembic import context
from src.core.config import get_settings


config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_online() -> None:
    db_config = get_settings().db
    connectable = create_engine(db_config.dsn, pool_pre_ping=True)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
