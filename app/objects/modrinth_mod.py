
from pydantic import BaseModel

class ModrinthMod(BaseModel):
    mod: str
    version: str