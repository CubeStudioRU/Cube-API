from typing import List

from fastapi.params import Depends

from app.core.utils import hash_dict
from app.integrations.base_integration import BaseIntegration
from app.integrations.curseforge_integration import get_curseforge_integration, CurseforgeIntegration
from app.integrations.modrinth_integration import get_modrinth_integration, ModrinthIntegration
from app.schemas.instance_schema import CompiledInstance, Instance, InstanceType, CachedInstance
from app.services.compile_cache_service import CompileCacheService, get_compile_cache_service
from app.services.instance_service import InstanceService, get_instance_service


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

        cached_instance = await self.cache_service.get_valid_cache(instance)
        if cached_instance:
            return cached_instance

        compiled_instance = await self.compile_instance(instance, instance_type)
        await self.cache_instance(instance, compiled_instance)

        return compiled_instance

    async def cache_instance(self, instance: Instance, compiled_instance: CompiledInstance) -> None:
        cached_instance = CachedInstance(**compiled_instance.model_dump(), hash=hash_dict(instance.model_dump()))
        await self.cache_service.add_cache(cached_instance)

    async def compile_instance(self, instance: Instance, instance_type: InstanceType) -> CompiledInstance:
        compiled_instance_mods = []

        for integration in self.integrations:
            try:
                mods = await integration.extract_mods(instance)
                compiled_instance_mods += await integration.get_mods(mods, instance_type)
            except Exception as e:
                print(f"Error in integration {integration.__str__()}: {e}")

        compiled_instance = CompiledInstance(
            uuid=instance.uuid,
            name=instance.name,
            version=instance.version,
            changelog=instance.changelog,
            mods=compiled_instance_mods,
            instance_type=instance_type
        )
        return compiled_instance


async def get_compile_service(instance_service: InstanceService = Depends(get_instance_service),
                              compile_cache_service: CompileCacheService = Depends(
                                  get_compile_cache_service),
                              modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
                              curseforge_integration: CurseforgeIntegration = Depends(
                                  get_curseforge_integration)) -> CompileService:
    integrations: List[BaseIntegration] = [
        modrinth_integration,
        curseforge_integration
    ]

    return CompileService(
        instance_service,
        compile_cache_service,
        integrations
    )
