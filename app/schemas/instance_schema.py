from enum import Enum

from pydantic import BaseModel, ConfigDict

from app.schemas.cache_schema import Cached
from app.schemas.content_schema import CompiledContentContainer


class InstanceType(str, Enum):
    server = "server"
    client = "client"
    both = "both"


class BaseInstance(BaseModel):
    model_config = ConfigDict(extra="ignore")
    uuid: str
    name: str
    version: str
    changelog: str


class Instance(BaseInstance):
    game_version: str
    loader: str


class CompiledInstance(BaseInstance):
    instance_type: InstanceType
    containers: list[CompiledContentContainer]


class CachedInstance(CompiledInstance, Cached):
    pass
