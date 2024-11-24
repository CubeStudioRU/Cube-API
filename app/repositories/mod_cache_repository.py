from abc import ABC

from app.repositories.base_repository import BaseRepository
from app.schemas.mod_schema import CachedMod


class ModCacheRepository(BaseRepository[CachedMod], ABC):
    pass
