from enum import Enum
from typing import List

from pydantic import BaseModel

from app.schemas.mod_schema import ModrinthMod, CurseforgeMod, CompiledMod


class BaseInstance(BaseModel):
    id: int
    name: str
    version: str
    changelog: str


class Instance(BaseInstance):
    game_version: str
    loader: str
    modrinth: List[ModrinthMod]
    curseforge: List[CurseforgeMod]


class CompiledInstance(BaseInstance):
    instance_hash: str
    mods: List[CompiledMod]


class InstanceType(str, Enum):
    server = "server"
    client = "client"
