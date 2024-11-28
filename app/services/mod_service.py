from collections.abc import Sequence
from typing import List

from fastapi.params import Depends

from app.core.utils import hash_dict
from app.integrations.base_integration import BaseIntegration
from app.integrations.curseforge_integration import get_curseforge_integration, CurseforgeIntegration
from app.integrations.modrinth_integration import get_modrinth_integration, ModrinthIntegration
from app.repositories.mod_content_repository import ModContentRepository
from app.repositories.mongo.mongo_mod_content_repository import MongoModContentRepository
from app.schemas.content_schema import CompiledContent, ContentSide
from app.schemas.instance_schema import InstanceType


class ModService:
    def __init__(self, repository: ModContentRepository, integrations: List[BaseIntegration]):
        self.repository = repository
        self.integrations = integrations

    async def get_compiled_mods(self, instance_type: InstanceType) -> List[CompiledContent]:
        mod_sides = ContentSide.from_instance_type(instance_type)
        compiled_mods: List[CompiledContent] = []

        for integration in self.integrations:
            mods = await self.repository.get_typed_by_integration_and_sides(integration.integration_type, mod_sides)
            compiled_mods.extend(await integration.get_contents(mods))

        return compiled_mods

    async def get_mods_hash(self) -> str:
        mods = await self.repository.get_all()
        return hash_dict({"mods": mods})


IntegrationList = Sequence[BaseIntegration]


async def get_mod_service(repository: ModContentRepository = Depends(MongoModContentRepository),
                          modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
                          curseforge_integration: CurseforgeIntegration = Depends(
                              get_curseforge_integration)) -> ModService:
    integrations = [
        modrinth_integration,
        curseforge_integration
    ]
    return ModService(repository, integrations)
