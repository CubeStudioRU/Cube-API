from app.core.config import COMPILED_INSTANCE_VAULT
from app.core.utils import hash_dict
from app.schemas.instance_schema import Instance, InstanceType, CompiledInstance
from app.services.cache_service import CacheService, JsonVaultCacheService


class CompileCacheService:
    def __init__(self, cache_service: CacheService):
        self.cache_service = cache_service

    async def get_valid_cached_instance(self, instance: Instance,
                                        instance_type: InstanceType) -> CompiledInstance | None:
        cached_instance = await self.get_cached_instance(instance_type)
        if cached_instance and hash_dict(instance.model_dump()) == cached_instance.instance_hash:
            return cached_instance
        return None

    async def get_cached_instance(self, instance_type: InstanceType) -> CompiledInstance | None:
        data = await self.cache_service.get(instance_type.name)
        if data is None:
            return None
        return CompiledInstance.model_validate(data)

    async def update_cached_instance(self, instance: CompiledInstance, instance_type: InstanceType):
        await self.cache_service.set(instance_type.name, instance.model_dump())


async def compile_cache_service_factory(cache_service: CacheService = None) -> CompileCacheService:
    if cache_service is None:
        cache_service = JsonVaultCacheService(COMPILED_INSTANCE_VAULT)
    return CompileCacheService(cache_service)
