from fastapi.params import Depends

from app.core.utils import hash_dict
from app.schemas.instance_schema import CompiledInstance, Instance, InstanceType, CachedInstance
from app.services.compile_cache_service import CompileCacheService, get_compile_cache_service
from app.services.instance_service import InstanceService, get_instance_service
from app.services.mod_service import ModService, get_mod_service


class CompileService:
    def __init__(self,
                 instance_service: InstanceService,
                 mod_service: ModService,
                 cache_service: CompileCacheService):
        self.instance_service = instance_service
        self.mod_service = mod_service
        self.cache_service = cache_service

    async def get_compiled_instance(self, instance_type: InstanceType) -> CompiledInstance:
        instance: Instance = await self.instance_service.get_instance()

        cached_instance = await self.cache_service.get_valid_instance_cache(instance, instance_type)
        if cached_instance:
            return cached_instance

        compiled_instance = await self.compile_instance(instance, instance_type)
        await self.cache_instance(instance, compiled_instance)

        return compiled_instance

    async def cache_instance(self, instance: Instance, compiled_instance: CompiledInstance) -> None:
        cached_instance = CachedInstance(**compiled_instance.model_dump(), hash=hash_dict(instance.model_dump()))
        await self.cache_service.add_cache(cached_instance)

    async def compile_instance(self, instance: Instance, instance_type: InstanceType) -> CompiledInstance:
        mods = await self.mod_service.get_compiled_mods(instance_type)

        compiled_instance = CompiledInstance(
            uuid=instance.uuid,
            name=instance.name,
            version=instance.version,
            changelog=instance.changelog,
            mods=mods,
            instance_type=instance_type
        )
        return compiled_instance


async def get_compile_service(instance_service: InstanceService = Depends(get_instance_service),
                              mod_service: ModService = Depends(get_mod_service),
                              compile_cache_service: CompileCacheService = Depends(
                                  get_compile_cache_service)) -> CompileService:
    return CompileService(
        instance_service,
        mod_service,
        compile_cache_service,
    )
