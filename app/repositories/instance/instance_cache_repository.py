from abc import ABC

from app.repositories.cache_repository import CacheRepository


class InstanceCacheRepository(CacheRepository, ABC):
    repository_name = "cached_instances"
