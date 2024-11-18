from typing import Dict

from pydantic import BaseModel

class CompiledInstanceMod(BaseModel):
    file: str
    url: str