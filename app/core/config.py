from functools import lru_cache

from dotenv import load_dotenv
from pydantic import computed_field
from pydantic.v1 import BaseSettings

load_dotenv('.env')

COMPILED_INSTANCE_VAULT = './instance/'
INSTANCE_FILE = './instance/instance.json'


class Settings(BaseSettings):
    ENV: str = "prod"
    PROJECT_NAME: str = "Cube-API"

    backend_port: str

    curseforge_api_key: str

    mongo_root_user: str
    mongo_root_pass: str
    mongo_port: str

    class Config:
        env_file = ".env"
        extra = "allow"
        case_sensitive = False


class MongoSettings(BaseSettings):
    mongo_root_user: str
    mongo_root_pass: str
    mongo_port: str

    @computed_field
    @property
    def mongodb_url(self) -> str:
        return f"mongodb://{self.mongo_root_user}:{self.mongo_root_pass}@mongo:{self.mongo_port}/"

    class Config:
        extra = "allow"
        env_file = ".env"


@lru_cache()
def get_mongo_settings():
    return MongoSettings()


@lru_cache()
def get_settings():
    return Settings()
