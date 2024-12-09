from typing_extensions import TypeVar

from app.repositories.content_repository import ContentRepository
from app.repositories.repositories_mongo.mongo_base_repository import (
    MongoBaseRepository,
)
from app.schemas.content_schema import ContentSide, TypedContent
from app.schemas.integration_schema import IntegrationType

T = TypeVar("T")


class MongoContentRepository(MongoBaseRepository, ContentRepository):
    entity_model = TypedContent

    async def get_all(self) -> list[TypedContent]:
        documents = await self.storage.find_all(self.repository_name, {})
        return [
            self.entity_model.model_validate({**document, "content_type": self.repository_name})
            for document in documents
        ]

    async def get(self, entity_uuid: str) -> T | None:
        return None

    async def get_typed_by_integration(self, integration_type: IntegrationType) -> list[TypedContent]:
        documents = await self.storage.find_all(self.repository_name, {"integration": integration_type.name})
        return [
            self.entity_model.model_validate({**document, "content_type": self.repository_name})
            for document in documents
        ]

    async def get_typed_by_sides(self, sides: list[ContentSide]) -> list[TypedContent]:
        documents = await self.storage.find_all(self.repository_name, {"side": {"$in": sides}})
        return [
            self.entity_model.model_validate({**document, "content_type": self.repository_name})
            for document in documents
        ]

    async def get_typed_by_integration_and_sides(
        self, integration_type: IntegrationType, sides: list[ContentSide]
    ) -> list[TypedContent]:
        documents = await self.storage.find_all(
            self.repository_name,
            {"integration": integration_type.name, "side": {"$in": sides}},
        )
        return [
            self.entity_model.model_validate({**document, "content_type": self.repository_name})
            for document in documents
        ]
