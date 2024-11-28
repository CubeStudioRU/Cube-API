from abc import ABC

from app.repositories.cache_repository import CacheRepository


class ContentCacheRepository(CacheRepository, ABC):
    pass
