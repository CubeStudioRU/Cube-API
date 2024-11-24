from abc import ABC, abstractmethod
from typing import List

from app.schemas.instance_schema import Instance, InstanceType
from app.schemas.mod_schema import ModSide, IntegrationMod, CompiledMod


class BaseIntegration(ABC):
    BASE_URL: str

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
                compiled_mods.append(await self.get_mod(mod))

        return compiled_mods

    @abstractmethod
    async def extract_mods(self, instance: Instance) -> List[IntegrationMod]:
        pass
