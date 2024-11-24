from abc import ABC

from app.repositories.cache_repository import CacheRepository


class InstanceCacheRepository(CacheRepository, ABC):
    pass
