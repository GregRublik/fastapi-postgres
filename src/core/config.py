from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DbSettings(BaseSettings):
    db_host: str = Field(json_schema_extra={'env': 'DB_HOST'})
    db_user: str = Field(json_schema_extra={'env': 'DB_USER'})
    db_pass: str = Field(json_schema_extra={'env': 'DB_PASS'})
    db_name: str = Field(json_schema_extra={'env': 'DB_NAME'})
    db_port: int = Field(json_schema_extra={'env': 'DB_PORT'})

    # class Config:
    #     env_prefix = "DB_"

    model_config = SettingsConfigDict(env_prefix="DB_", env_file=".env", extra="ignore")

    @property
    def dsn(self):
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def dsn_asyncpg(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


class Settings(BaseSettings):
    app_port: int = Field(json_schema_extra={'env': 'DB_HOST'})

    db: DbSettings

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env", extra="ignore")


settings = Settings(db=DbSettings())
