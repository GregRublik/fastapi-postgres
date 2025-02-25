from pydantic_settings import BaseSettings
from pydantic import Field


class DbSettings(BaseSettings):
    db_host: str = Field(json_schema_extra={'env': 'DB_HOST'})
    db_user: str = Field(json_schema_extra={'env': 'DB_USER'})
    db_pass: str = Field(json_schema_extra={'env': 'DB_PASS'})
    db_name: str = Field(json_schema_extra={'env': 'DB_NAME'})
    db_port: int = Field(json_schema_extra={'env': 'DB_PORT'})

    class Config:
        env_prifix = "DB_"

    @property
    def dsn(self):
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def dsn_asyncpg(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


class Settings(BaseSettings):
    db: DbSettings


def get_settings():
    return Settings(
        db=DbSettings()
    )
