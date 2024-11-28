from app.repositories.cache_repository import CacheRepository
from app.repositories.repositories_mongo.mongo_base_repository import MongoBaseRepository
from app.schemas.cache_schema import Cached


class MongoCacheRepository(MongoBaseRepository, CacheRepository):
    entity_model = Cached

    async def get(self, entity_hash: str) -> entity_model:
        document = await self.storage.find_one(self.repository_name, {"hash": entity_hash})
        return self.entity_model.model_validate(document) if document else None

    async def delete(self, entity: Cached) -> None:
        await self.storage.delete_one(self.repository_name, {"hash": entity.hash})
