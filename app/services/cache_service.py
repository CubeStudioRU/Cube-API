from pydantic import BaseModel
from typing_extensions import TypeVar

from app.core.utils import hash_dict
from app.repositories.cache_repository import CacheRepository
from app.schemas.cache_schema import Cached

Entity = TypeVar("Entity", bound=BaseModel)
CachedEntity = TypeVar("CachedEntity", bound=Cached)


class CacheService(Entity, CachedEntity):
    def __init__(self, repository: CacheRepository):
        self.repository = repository

    async def get_valid_cache(self, entity: Entity, entity_hash: str) -> CachedEntity | None:
        cached = await self.get_cache(entity_hash)
        if cached and hash_dict(entity.model_dump()) == cached.hash:
            return cached
        return None

    async def get_cache(self, entity_hash: str) -> CachedEntity | None:
        return await self.repository.get(entity_hash)

    async def delete_cache(self, entity_hash: str) -> None:
        cached = await self.get_cache(entity_hash)
        if cached:
            await self.repository.delete(cached)

    async def update_cache(self, cached_entity: CachedEntity):
        await self.repository.save(cached_entity)
