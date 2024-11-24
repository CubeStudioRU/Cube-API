from abc import ABC

from app.repositories.cache_repository import CacheRepository


class ModCacheRepository(CacheRepository, ABC):
    repository_name = "cached_mods"
