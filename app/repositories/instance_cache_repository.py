from abc import ABC

from app.repositories.base_repository import BaseRepository
from app.schemas.instance_schema import CachedInstance


class InstanceCacheRepository(BaseRepository[CachedInstance], ABC):
    pass
