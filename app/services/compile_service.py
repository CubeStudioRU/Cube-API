from typing import List

from app.core.utils import hash_dict
from app.integrations.base_integration import BaseIntegration
from app.integrations.curseforge_integration import curseforge_integration
from app.integrations.modrinth_integration import modrinth_integration
from app.schemas.instance_schema import CompiledInstance, Instance, InstanceType
from app.services.cache_service import compile_cache_service_factory, CompileCacheService
from app.services.instance_service import InstanceService, instance_service_factory


class CompileService:
    def __init__(self,
                 compile_instance_service: InstanceService,
                 cache_service: CompileCacheService,
                 integrations: List[BaseIntegration]):
        self.instance_service = compile_instance_service
        self.cache_service = cache_service
        self.integrations = integrations

    async def get_compiled_instance(self, instance_type: InstanceType) -> CompiledInstance:
        instance: Instance = await self.instance_service.get_instance()

        # cached_instance = await self.cache_service.get_valid_cached_instance(instance)
        # if cached_instance:
        #    return cached_instance

        compiled_instance = await self.compile_instance(instance, instance_type)
        await self.cache_service.update_cached_instance(compiled_instance)

        return compiled_instance

    async def compile_instance(self, instance: Instance, instance_type: InstanceType) -> CompiledInstance:
        compiled_instance_mods = []

        for integration in self.integrations:
            try:
                mods = await integration.extract_mods(instance)
                compiled_instance_mods += await integration.get_mods(mods, instance_type)
            except Exception as e:
                print(f"Error in integration {integration.__repr__()}: {e}")

        compiled_instance = CompiledInstance(
            id=instance.id,
            name=instance.name,
            version=instance.version,
            changelog=instance.changelog,
            instance_hash=hash_dict(instance.model_dump()),
            mods=compiled_instance_mods
        )
        return compiled_instance


async def compile_service_factory() -> CompileService:
    instance_service = await instance_service_factory()
    compile_cache_service = await compile_cache_service_factory()
    integrations: List[BaseIntegration] = [
        curseforge_integration,
        modrinth_integration,
    ]

    return CompileService(
        instance_service,
        compile_cache_service,
        integrations
    )


async def get_compile_service() -> CompileService:
    return await compile_service_factory()
