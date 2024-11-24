from typing import List, Optional, TypeVar

from app.repositories.base_repository import BaseRepository
from app.storage.mongo_storage import AsyncMongoStorage

T = TypeVar('T')


class MongoBaseRepository(BaseRepository):
    collection_name: str

    def __init__(self, storage: AsyncMongoStorage):
        self.storage = storage

    async def get_all(self) -> List[T]:
        documents = await self.storage.find_all(self.collection_name)
        return [T.model_validate(**doc) for doc in documents]

    async def get(self, entity_id: str) -> Optional[T]:
        document = await self.storage.find_one(self.collection_name, {"id": entity_id})
        return T.model_validate(**document) if document else None

    async def save(self, entity: T) -> None:
        await self.storage.insert_one(self.collection_name, entity.model_dump())

    async def delete(self, entity: T) -> None:
        await self.storage.delete_one(self.collection_name, {"id": entity.id})
