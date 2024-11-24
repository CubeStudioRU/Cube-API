from abc import abstractmethod, ABC
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


class BaseRepository(ABC, Generic[T]):
    repository_name: str

    @abstractmethod
    async def get_all(self) -> List[T]:
        pass

    @abstractmethod
    async def get(self, entity_id: str) -> Optional[T]:
        pass

    @abstractmethod
    async def save(self, entity: T) -> None:
        pass

    @abstractmethod
    async def delete(self, entity: T) -> None:
        pass
