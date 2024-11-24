from functools import lru_cache

from dotenv import load_dotenv
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
        case_sensitive = False


@lru_cache()
def get_settings():
    return Settings()
