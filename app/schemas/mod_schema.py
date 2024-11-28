from enum import Enum

from pydantic import ConfigDict

from app.schemas.cache_schema import Cached
from app.schemas.content_schema import BaseContent


class IntegrationType(str, Enum):
    modrinth = "modrinth"
    curseforge = "curseforge"


class ModSide(str, Enum):
    server = "server"
    client = "client"
    both = "both"

    @classmethod
    def from_instance_type(cls, instance_type) -> list["ModSide"]:
        sides = [cls.both]
        if instance_type == "client":
            sides.append(cls.client)
        if instance_type == "server":
            sides.append(cls.server)
        if instance_type == "both":
            sides.extend((cls.server, cls.client))
        return sides


class BaseMod(BaseContent):
    model_config = ConfigDict(extra='ignore')
    pass


class IntegrationMod(BaseMod):
    mod: str
    version: str
    side: ModSide
    integration: IntegrationType


class CompiledMod(BaseMod):
    file: str
    url: str


class CachedMod(CompiledMod, Cached):
    pass
