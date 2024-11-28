from fastapi import Depends

from app.repositories.mod_content_cache_repository import ModContentCacheRepository
from app.repositories.mongo.mongo_mod_content_cache_repository import MongoModContentCacheRepository
from app.schemas.mod_content_schema import ModContent, ModCachedContent
from app.services.cache_service import CacheService


class ModCacheService(CacheService[ModContent, ModCachedContent]):
    pass


async def get_mod_cache_service(mod_cache_repository: ModContentCacheRepository = Depends(
    MongoModContentCacheRepository)) -> ModCacheService:
    return ModCacheService(mod_cache_repository)
