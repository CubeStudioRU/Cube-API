from typing import Optional

from typing_extensions import TypeVar

from app.repositories.instance_cache_repository import InstanceCacheRepository
from app.repositories.mongo.mongo_base_repository import MongoBaseRepository

T = TypeVar("T")


class MongoCacheRepository(InstanceCacheRepository, MongoBaseRepository):
    def __init__(self):
        super().__init__()

    async def get(self, entity_hash: str) -> Optional[T]:
        document = await self.storage.find_one(self.collection_name, {"hash": entity_hash})
        return T.model_validate(**document) if document else None

    async def delete(self, entity: T) -> None:
        await self.storage.delete_one(self.collection_name, {"hash": entity.hash})
