from typing import Generic, TypeVar

from fastapi import Depends
from pydantic import BaseModel

from app.repositories.base_repository import BaseRepository
from app.storage.mongo_storage import AsyncMongoStorage, get_async_mongo_storage

Entity = TypeVar("Entity", bound=BaseModel)


class MongoBaseRepository(BaseRepository, Generic[Entity]):
    entity_model: BaseModel

    def __init__(self, storage: AsyncMongoStorage = Depends(get_async_mongo_storage)):
        self.storage = storage

    async def get_all(self) -> list[Entity]:
        documents = await self.storage.find_all(self.repository_name)
        return [self.entity_model.model_validate(doc) for doc in documents]

    async def get(self, entity_uuid: str) -> Entity | None:
        document = await self.storage.find_one(self.repository_name, {"uuid": entity_uuid})
        return self.entity_model.model_validate(document) if document else None

    async def save(self, entity: Entity) -> None:
        await self.storage.insert_one(self.repository_name, entity.model_dump())

    async def delete(self, entity: Entity) -> None:
        await self.storage.delete_one(self.repository_name, {"id": entity.id})
