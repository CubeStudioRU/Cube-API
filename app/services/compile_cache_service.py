from fastapi.params import Depends

from app.repositories.instance_cache_repository import InstanceCacheRepository
from app.repositories.mongo.mongo_instance_cache_repository import MongoInstanceCacheRepository
from app.schemas.instance_schema import Instance, CachedInstance, InstanceType
from app.services.cache_service import CacheService


class CompileCacheService(CacheService[Instance, CachedInstance]):
    def __init__(self, repository: InstanceCacheRepository):
        super().__init__(repository)

    async def get_valid_instance_cache(self, entity_hash: str, entity_type: InstanceType) -> CachedInstance | None:
        cached = await self.get_instance_cache(entity_hash, entity_type)
        if cached and entity_hash == cached.hash:
            return cached
        return None

    async def get_instance_cache(self, entity_hash: str, entity_type: InstanceType) -> CachedInstance | None:
        return await self.repository.get_instance(entity_hash, entity_type)


async def get_compile_cache_service(instance_cache_repository: InstanceCacheRepository = Depends(
    MongoInstanceCacheRepository)) -> CompileCacheService:
    return CompileCacheService(instance_cache_repository)
