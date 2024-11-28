from enum import Enum

from pydantic import BaseModel


class BaseContent(BaseModel):
    pass


class ContentSide(str, Enum):
    client = "client"
    server = "server"
    both = "both"
