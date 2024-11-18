from typing import Iterable

from app.core.config import COMPILED_INSTANCE_FILE
from app.core.utils import hash_dict
from app.crud.files import get_json, save_json
from app.integrations.base_integration import BaseIntegration
from app.integrations.curseforge_integration import curseforge_integration
from app.integrations.modrinth_integration import modrinth_integration
from app.schemas.instance_schema import CompiledInstance, Instance
from app.services.instance_service import InstanceService


class CompileService:
    @staticmethod
    async def get_compiled_instance() -> CompiledInstance:
        instance: Instance = await InstanceService.get_instance()

        if await CompiledCacheService.is_cache_vaild(instance):
            return await CompiledCacheService.get_cached_instance()

        compiled_instance = await CompileService.compile_instance(instance)
        await CompiledCacheService.update_cached_instance(compiled_instance)

        return compiled_instance

    @staticmethod
    async def compile_mods(integration: BaseIntegration, data: Iterable):
        return [await integration.get_mod(mod) for mod in data]

    @staticmethod
    async def compile_instance(instance: Instance) -> CompiledInstance:
        compiled_instance_mods = []

        compiled_instance_mods += await CompileService.compile_mods(modrinth_integration, instance.modrinth)
        compiled_instance_mods += await CompileService.compile_mods(curseforge_integration, instance.curseforge)

        compiled_instance = CompiledInstance(
            id=instance.id,
            name=instance.name,
            version=instance.version,
            changelog=instance.changelog,
            instance_hash=hash_dict(instance.model_dump()),
            mods=compiled_instance_mods
        )

        return compiled_instance


class CompiledCacheService:
    @staticmethod
    async def is_cache_vaild(instance: Instance) -> bool:
        cached_instance = await CompiledCacheService.get_cached_instance()
        if cached_instance is None:
            return False
        if hash_dict(instance.model_dump()) == cached_instance.instance_hash:
            return True
        return False

    @staticmethod
    async def get_cached_instance() -> CompiledInstance | None:
        data = get_json(COMPILED_INSTANCE_FILE)
        if data is None:
            return None
        return CompiledInstance.model_validate(data)

    @staticmethod
    async def update_cached_instance(instance: CompiledInstance):
        save_json(instance.model_dump(), COMPILED_INSTANCE_FILE)
