from abc import ABC, abstractmethod
from typing import List

from app.schemas.instance_schema import Instance
from app.schemas.mod_schema import BaseMod, CompiledInstanceMod


class BaseIntegration(ABC):
    BASE_URL: str

    @abstractmethod
    async def get_mod(self, mod: BaseMod) -> CompiledInstanceMod:
        pass

    async def get_mods(self, mods: List[BaseMod]) -> List[CompiledInstanceMod]:
        return [await self.get_mod(mod) for mod in mods]

    @abstractmethod
    async def extract_mods(self, instance: Instance) -> List[BaseMod]:
        pass
