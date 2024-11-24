from abc import ABC, abstractmethod
from typing import List

from app.core.utils import hash_dict
from app.schemas.instance_schema import Instance, InstanceType
from app.schemas.mod_schema import ModSide, IntegrationMod, CompiledMod, CachedMod
from app.services.mod_cache_service import ModCacheService


class BaseIntegration(ABC):
    BASE_URL: str

    def __init__(self, cache_service: ModCacheService):
        self.cache_service = cache_service

    @abstractmethod
    async def get_mod(self, mod: IntegrationMod) -> CompiledMod:
        pass

    async def get_mods(self, mods: List[IntegrationMod], instance_type: InstanceType) -> List[CompiledMod]:
        supported_mods = [ModSide.both]
        if instance_type == InstanceType.client:
            supported_mods.append(ModSide.client)
        elif instance_type == InstanceType.server:
            supported_mods.append(ModSide.server)

        compiled_mods = []

        for mod in mods:
            if mod.side in supported_mods:
                cached_mod = await self.cache_service.get_valid_cache(mod)
                if cached_mod:
                    compiled_mods.append(cached_mod)
                else:
                    compiled_mod = await self.get_mod(mod)
                    if compiled_mod:
                        await self.cache_mod(mod, compiled_mod)
                        compiled_mods.append(compiled_mod)
                    else:
                        print(f"{mod.model_dump()} Failed")

        return compiled_mods

    async def cache_mod(self, integration_mod: IntegrationMod, compiled_mod: CompiledMod):
        cached_mod = CachedMod(**compiled_mod.model_dump(), hash=hash_dict(integration_mod.model_dump()))
        await self.cache_service.add_cache(cached_mod)

    @abstractmethod
    async def extract_mods(self, instance: Instance) -> List[IntegrationMod]:
        pass
