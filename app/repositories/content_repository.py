from abc import ABC
from typing import List

from app.repositories.base_repository import BaseRepository
from app.schemas.content_schema import BaseContent, ContentSide, TypedContent
from app.schemas.integration_schema import IntegrationType


class ContentRepository(BaseRepository[BaseContent], ABC):

    async def get_typed_by_integration(self, integration_type: IntegrationType) -> List[TypedContent]:
        pass

    async def get_typed_by_sides(self, sides: List[ContentSide]) -> List[TypedContent]:
        pass

    async def get_typed_by_integration_and_sides(self, integration_type: IntegrationType, sides: List[ContentSide]) -> \
    List[
        TypedContent]:
        pass
