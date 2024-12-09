from enum import Enum

from pydantic import BaseModel, ConfigDict

from app.schemas.cache_schema import Cached
from app.schemas.integration_schema import IntegrationType


class ContentType(str, Enum):
    mods = "mods"
    resourcepacks = "resourcepacks"


class ContentSide(str, Enum):
    client = "client"
    server = "server"
    both = "both"

    @classmethod
    def from_instance_type(cls, instance_type) -> list["ContentSide"]:
        sides = [cls.both]
        if instance_type == "client":
            sides.append(cls.client)
        if instance_type == "server":
            sides.append(cls.server)
        if instance_type == "both":
            sides.extend((cls.server, cls.client))
        return sides


class Content(BaseModel):
    model_config = ConfigDict(extra="ignore")


class BaseContent(Content):
    side: ContentSide
    integration: IntegrationType


class TypedContent(BaseContent):
    content_type: ContentType


class CompiledContent(Content):
    file: str
    url: str


class CachedContent(CompiledContent, Cached):
    pass


class IntegrationContent(BaseContent):
    project: str
    version: str


class CompiledContentContainer(BaseModel):
    content_type: ContentType
    content: list[CompiledContent]
