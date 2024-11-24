from pydantic import BaseModel


class Cached(BaseModel):
    hash: str
