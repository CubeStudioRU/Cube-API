from typing import List, Optional

from typing_extensions import TypeVar

from app.repositories.content_repository import ContentRepository
from app.repositories.mongo.mongo_base_repository import MongoBaseRepository
from app.schemas.content_schema import BaseContent, ContentSide
from app.schemas.mod_schema import IntegrationType

T = TypeVar("T")


class MongoContentRepository(MongoBaseRepository, ContentRepository):
    entity_model = BaseContent

    async def get(self, entity_uuid: str) -> Optional[T]:
        return None

    async def get_by_integration(self, integration_type: IntegrationType) -> List[BaseContent]:
        documents = await self.storage.find_all(self.repository_name, {"integration": integration_type.name})
        return [self.entity_model.model_validate(document) for document in documents]

    async def get_by_sides(self, sides: List[ContentSide]) -> List[BaseContent]:
        documents = await self.storage.find_all(self.repository_name, {"side": {"$in": sides}})
        return [self.entity_model.model_validate(document) for document in documents]

    async def get_by_integration_and_sides(self, integration_type: IntegrationType, sides: List[ContentSide]) -> List[
        BaseContent]:
        documents = await self.storage.find_all(self.repository_name,
                                                {"integration": integration_type.name, "side": {"$in": sides}})
        return [self.entity_model.model_validate(document) for document in documents]
