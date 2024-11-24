from abc import ABC

from app.repositories.base_repository import BaseRepository
from app.schemas.cache_schema import Cached


class CacheRepository(BaseRepository[Cached], ABC):
    repository_name = "cached"
