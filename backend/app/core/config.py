from pathlib import Path
from typing import ClassVar

from pydantic_settings import BaseSettings
import diskcache as dc

class Settings(BaseSettings):
    DATABASE_CONFIG : ClassVar[dict] = {
        'dbname': 'paleoclimate',
        'user': 'paleoclimate',
        'password': 'paleoclimate',
        'host': 'postgres',
        'port': '5432',
    }
    DATABASE_URL: str = f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['dbname']}"
    ROOT_PATH: Path = Path("../")
    RESOURCE_PATH: Path = Path("../../")
    CACHE: ClassVar[dc.Cache] = dc.Cache('./model_cache')


settings = Settings()
