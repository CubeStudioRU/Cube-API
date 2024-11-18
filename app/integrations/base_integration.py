from abc import ABC, abstractmethod

from app.schemas.mod_schema import BaseMod, CompiledInstanceMod


class BaseIntegration(ABC):
    BASE_URL: str

    @abstractmethod
    async def get_mod(self, mod: BaseMod) -> CompiledInstanceMod:
        pass
