from typing import List

from pydantic import BaseModel

from .compiled_instance_mod import CompiledInstanceMod

class CompiledInstance(BaseModel):
    id: int
    name: str
    version: str
    changelog: str
    mods: List[CompiledInstanceMod]