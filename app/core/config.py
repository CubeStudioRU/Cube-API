from pydantic.v1 import BaseSettings


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

    @property
    def mongodb_url(self) -> str:
        return f"mongodb://{self.mongo_root_user}:{self.mongo_root_pass}@mongo:27017"

    class Config:
        extra = "allow"
        env_file = ".env"


def get_mongo_settings():
    return MongoSettings()


def get_settings():
    return Settings()
