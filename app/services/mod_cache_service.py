from fastapi import Depends

from app.repositories.mod_cache_repository import ModCacheRepository
from app.repositories.mongo.mongo_mod_cache_repository import MongoModCacheRepository
from app.schemas.mod_schema import IntegrationMod, CachedMod
from app.services.cache_service import CacheService


class ModCacheService(CacheService[IntegrationMod, CachedMod]):
    pass


async def get_mod_cache_service(mod_cache_repository: ModCacheRepository = Depends(
    MongoModCacheRepository)) -> ModCacheService:
    return ModCacheService(mod_cache_repository)
