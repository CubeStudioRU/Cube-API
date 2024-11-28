from abc import ABC

from app.repositories.content_cache_repository import ContentCacheRepository


class ModContentCacheRepository(ContentCacheRepository, ABC):
    repository_name = "cached_mods"
