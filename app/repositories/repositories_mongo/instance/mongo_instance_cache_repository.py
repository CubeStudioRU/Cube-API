from app.repositories.instance.instance_cache_repository import InstanceCacheRepository
from app.repositories.repositories_mongo.mongo_cache_repository import (
    MongoCacheRepository,
)
from app.schemas.instance_schema import CachedInstance, InstanceType


class MongoInstanceCacheRepository(MongoCacheRepository, InstanceCacheRepository):
    entity_model = CachedInstance

    async def get_instance(self, entity_hash: str, entity_type: InstanceType) -> entity_model:
        document = await self.storage.find_one(
            self.repository_name,
            {"hash": entity_hash, "instance_type": entity_type.value},
        )
        return self.entity_model.model_validate(document) if document else None

    async def delete_instance(self, entity: CachedInstance, entity_type: InstanceType) -> None:
        await self.storage.delete_one(
            self.repository_name,
            {"hash": entity.hash, "instance_type": entity_type.value},
        )
