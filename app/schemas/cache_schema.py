from pydantic import BaseModel, ConfigDict


class Cached(BaseModel):
    model_config = ConfigDict(extra="ignore")
    hash: str
