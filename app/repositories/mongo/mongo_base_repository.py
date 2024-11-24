from typing import List, Optional, TypeVar

from app.repositories.base_repository import BaseRepository
from app.storage.mongo_storage import AsyncMongoStorage

T = TypeVar('T')


class MongoBaseRepository(BaseRepository):
    collection_name: str

    def __init__(self, storage: AsyncMongoStorage):
        self.storage = storage

    async def get_all(self) -> List[T]:
        async with self.storage:
            documents = await self.storage.find_all(self.collection_name)
        return [T.model_validate(**doc) for doc in documents]

    async def get(self, entity_uuid: str) -> Optional[T]:
        async with self.storage:
            document = await self.storage.find_one(self.collection_name, {"uuid": entity_uuid})
        return T.model_validate(**document) if document else None

    async def save(self, entity: T) -> None:
        async with self.storage:
            await self.storage.insert_one(self.collection_name, entity.model_dump())

    async def delete(self, entity: T) -> None:
        async with self.storage:
            await self.storage.delete_one(self.collection_name, {"id": entity.id})
