from fastapi import Depends

from app.repositories.mongo.mongo_resourcepack_content_cache_repository import MongoResourcepackContentCacheRepository
from app.repositories.resourcepack_content_cache_repository import ResourcepackContentCacheRepository
from app.schemas.resourcepack_content_schema import ResourcepackContent, ResourcepackCachedContent
from app.services.cache_service import CacheService


class ResourcepackContentCacheService(CacheService[ResourcepackContent, ResourcepackCachedContent]):
    pass


async def get_resourcepack_content_cache_service(cache_repository: ResourcepackContentCacheRepository = Depends(
    MongoResourcepackContentCacheRepository)) -> ResourcepackContentCacheService:
    return ResourcepackContentCacheService(cache_repository)
