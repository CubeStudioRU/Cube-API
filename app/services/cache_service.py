from abc import abstractmethod

from app.core.config import COMPILED_INSTANCE_FILE
from app.core.utils import hash_dict
from app.crud.files import get_json, save_json
from app.schemas.instance_schema import CompiledInstance, Instance


class CacheService:
    @abstractmethod
    async def get(self, key: str) -> dict | None:
        pass

    @abstractmethod
    async def set(self, key: str, value: dict) -> None:
        pass


class FileCacheService(CacheService):
    def __init__(self, file_path: str):
        self.file_path = file_path

    async def get(self, key: str) -> dict | None:
        data = get_json(self.file_path)
        return data

    async def set(self, key: str, value: dict) -> None:
        save_json(value, self.file_path)


class CompileCacheService:
    def __init__(self, cache_service: CacheService):
        self.cache_service = cache_service

    async def get_valid_cached_instance(self, instance: Instance) -> CompiledInstance | None:
        cached_instance = await self.get_cached_instance()
        if cached_instance and hash_dict(instance.model_dump()) == cached_instance.instance_hash:
            return cached_instance
        return None

    async def get_cached_instance(self) -> CompiledInstance | None:
        data = await self.cache_service.get("instance")
        if data is None:
            return None
        return CompiledInstance.model_validate(data)

    async def update_cached_instance(self, instance: CompiledInstance):
        await self.cache_service.set("instance", instance.model_dump())


async def compile_cache_service_factory(cache_service: CacheService = None) -> CompileCacheService:
    if cache_service is None:
        cache_service = FileCacheService(COMPILED_INSTANCE_FILE)
    return CompileCacheService(cache_service)
