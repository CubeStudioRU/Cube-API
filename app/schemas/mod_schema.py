from enum import Enum

from pydantic import BaseModel


class ModSide(str, Enum):
    server = "server"
    client = "client"
    both = "both"


class IntegrationMod(BaseModel):
    side: ModSide


class ModrinthMod(IntegrationMod):
    mod: str
    version: str


class CurseforgeMod(IntegrationMod):
    mod: str | None
    mod_id: int
    file_id: int


class CompiledMod(BaseModel):
    file: str
    url: str


class CachedMod(CompiledMod):
    hash: str
