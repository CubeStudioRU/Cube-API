from typing import Dict

from pydantic import BaseModel

class CompiledInstance(BaseModel):
    id: int
    name: str
    version: str
    changelog: str
    mods: Dict[str, str]