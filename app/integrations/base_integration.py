from abc import ABC, abstractmethod
from typing import List

from app.core.utils import hash_dict
from app.schemas.mod_schema import IntegrationMod, CompiledMod, CachedMod, IntegrationType
from app.services.mod_cache_service import ModCacheService


class BaseIntegration(ABC):
    BASE_URL: str
    integration_type: IntegrationType

    def __init__(self, cache_service: ModCacheService, integration_type: IntegrationType):
        self.cache_service = cache_service
        self.integration_type = integration_type

    @abstractmethod
    async def get_mod(self, mod: IntegrationMod) -> CompiledMod:
        pass

    async def get_mods(self, mods: List[IntegrationMod]) -> List[CompiledMod]:
        compiled_mods = []

        for mod in mods:
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
