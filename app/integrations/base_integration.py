from abc import ABC, abstractmethod

from app.schemas import CompiledInstanceMod


class BaseIntegration(ABC):
    BASE_URL: str

    @abstractmethod
    async def get_mod(self, **kwargs) -> CompiledInstanceMod:
        pass
