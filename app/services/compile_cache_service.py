from fastapi.params import Depends

from app.repositories.instance_cache_repository import InstanceCacheRepository
from app.repositories.mongo.mongo_instance_cache_repository import MongoInstanceCacheRepository
from app.schemas.instance_schema import Instance, CachedInstance
from app.services.cache_service import CacheService


class CompileCacheService(CacheService[Instance, CachedInstance]):
    pass


async def get_compile_cache_service(instance_cache_repository: InstanceCacheRepository = Depends(
    MongoInstanceCacheRepository)) -> CompileCacheService:
    return CompileCacheService(instance_cache_repository)
