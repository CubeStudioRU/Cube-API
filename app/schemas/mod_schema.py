from enum import Enum

from pydantic import BaseModel


class ModSide(str, Enum):
    server = "server"
    client = "client"
    both = "both"


class BaseMod(BaseModel):
    pass


class CompiledInstanceMod(BaseMod):
    file: str
    url: str
    side: ModSide


class ModrinthMod(BaseMod):
    mod: str
    version: str
    side: ModSide


class CurseforgeMod(BaseMod):
    mod: str | None
    mod_id: int
    file_id: int
    side: ModSide
