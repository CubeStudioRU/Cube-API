from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    repository_name: str

    @abstractmethod
    async def get_all(self) -> list[T]:
        pass

    @abstractmethod
    async def get(self, entity_id: str) -> T | None:
        pass

    @abstractmethod
    async def save(self, entity: T) -> None:
        pass

    @abstractmethod
    async def delete(self, entity: T) -> None:
        pass
