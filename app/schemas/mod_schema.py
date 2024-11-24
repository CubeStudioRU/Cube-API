from enum import Enum

from pydantic import BaseModel, ConfigDict

from app.schemas.cache_schema import Cached


class ModSide(str, Enum):
    server = "server"
    client = "client"
    both = "both"


class BaseMod(BaseModel):
    model_config = ConfigDict(extra='ignore')
    pass


class IntegrationMod(BaseMod):
    side: ModSide


class ModrinthMod(IntegrationMod):
    mod: str
    version: str


class CurseforgeMod(IntegrationMod):
    mod: str | None
    mod_id: int
    file_id: int


class CompiledMod(BaseMod):
    file: str
    url: str


class CachedMod(CompiledMod, Cached):
    pass
