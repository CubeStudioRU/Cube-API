from fastapi.params import Depends

from app.core.utils import hash_dict
from app.schemas.instance_schema import (
    CachedInstance,
    CompiledInstance,
    Instance,
    InstanceType,
)
from app.services.compile_cache_service import (
    CompileCacheService,
    get_compile_cache_service,
)
from app.services.compile_content_service import (
    CompileContentService,
    get_compile_content_service,
)
from app.services.instance_service import InstanceService, get_instance_service


class CompileService:
    def __init__(
        self,
        instance_service: InstanceService,
        compile_content_service: CompileContentService,
        cache_service: CompileCacheService,
    ):
        self.instance_service = instance_service
        self.compile_content_service = compile_content_service
        self.cache_service = cache_service

    async def get_compiled_instance(self, instance_type: InstanceType) -> CompiledInstance:
        instance: Instance = await self.instance_service.get_instance()

        instance_hash = await self.get_instance_hash(instance)
        cached_instance = await self.cache_service.get_valid_instance_cache(instance_hash, instance_type)
        if cached_instance:
            return cached_instance

        compiled_instance = await self.compile_instance(instance, instance_type)
        await self.cache_instance(instance, compiled_instance)

        return compiled_instance

    async def get_instance_hash(self, instance: Instance) -> str:
        instance_hash = hash_dict(instance.model_dump())
        content_hash = await self.compile_content_service.get_contents_hash()
        return instance_hash + content_hash

    async def cache_instance(self, instance: Instance, compiled_instance: CompiledInstance) -> None:
        instance_hash = await self.get_instance_hash(instance)
        cached_instance = CachedInstance(**compiled_instance.model_dump(), hash=instance_hash)
        await self.cache_service.add_cache(cached_instance)

    async def compile_instance(self, instance: Instance, instance_type: InstanceType) -> CompiledInstance:
        containers = await self.compile_content_service.get_compiled_contents(instance_type)
        return CompiledInstance(
            uuid=instance.uuid,
            name=instance.name,
            version=instance.version,
            changelog=instance.changelog,
            containers=containers,
            instance_type=instance_type,
        )


async def get_compile_service(
    instance_service: InstanceService = Depends(get_instance_service),
    compile_content_service: CompileContentService = Depends(get_compile_content_service),
    compile_cache_service: CompileCacheService = Depends(get_compile_cache_service),
) -> CompileService:
    return CompileService(
        instance_service,
        compile_content_service,
        compile_cache_service,
    )
