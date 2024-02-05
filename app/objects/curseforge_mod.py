
from pydantic import BaseModel

class CurseforgeMod(BaseModel):
    mod: str | None
    mod_id: int
    file_id: int