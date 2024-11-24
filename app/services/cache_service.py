from abc import abstractmethod

from app.crud.files import get_json, save_json


class CacheService:
    @abstractmethod
    async def get(self, key: str) -> dict | None:
        pass

    @abstractmethod
    async def set(self, key: str, value: dict) -> None:
        pass


class JsonVaultCacheService(CacheService):
    def __init__(self, vault_path: str):
        self.vault_path = vault_path

    async def get(self, key: str) -> dict | None:
        data = get_json(self.vault_path + f"/{key}.json")
        return data

    async def set(self, key: str, value: dict) -> None:
        save_json(value, self.vault_path + f"/{key}.json")
