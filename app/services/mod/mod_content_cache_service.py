from fastapi import Depends

from app.repositories.mod.mod_content_cache_repository import ModContentCacheRepository
from app.repositories.repositories_mongo.mod.mongo_mod_content_cache_repository import MongoModContentCacheRepository
from app.schemas.mod_content_schema import ModContent, ModCachedContent
from app.services.cache_service import CacheService


class ModContentCacheService(CacheService[ModContent, ModCachedContent]):
    pass


async def get_mod_cache_service(cache_repository: ModContentCacheRepository = Depends(
    MongoModContentCacheRepository)) -> ModContentCacheService:
    return ModContentCacheService(cache_repository)
