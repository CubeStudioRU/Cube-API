from pydantic import BaseModel


class BaseMod(BaseModel):
    pass


class CompiledInstanceMod(BaseMod):
    file: str
    url: str


class ModrinthMod(BaseMod):
    mod: str
    version: str


class CurseforgeMod(BaseMod):
    mod: str | None
    mod_id: int
    file_id: int
