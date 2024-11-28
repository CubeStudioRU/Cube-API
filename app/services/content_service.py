from abc import ABC
from typing import List

from app.core.utils import hash_dict
from app.integrations.base_integration import BaseIntegration
from app.repositories.content_repository import ContentRepository
from app.schemas.content_schema import CompiledContent, ContentSide
from app.schemas.instance_schema import InstanceType


class ContentService(ABC):
    def __init__(self, repository: ContentRepository, integrations: List[BaseIntegration]):
        self.repository = repository
        self.integrations = integrations

    async def get_compiled_contents(self, instance_type: InstanceType) -> List[CompiledContent]:
        content_sides = ContentSide.from_instance_type(instance_type)
        compiled_contents: List[CompiledContent] = []

        for integration in self.integrations:
            contents = await self.repository.get_typed_by_integration_and_sides(integration.integration_type,
                                                                                content_sides)
            compiled_contents.extend(await integration.get_contents(contents))

        return compiled_contents

    async def get_contents_hash(self) -> str:
        contents = await self.repository.get_all()
        return hash_dict({self.repository.repository_name: contents})
