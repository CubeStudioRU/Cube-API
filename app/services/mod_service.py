from collections.abc import Sequence
from typing import List

from fastapi.params import Depends

from app.integrations.base_integration import BaseIntegration
from app.integrations.curseforge_integration import get_curseforge_integration, CurseforgeIntegration
from app.integrations.modrinth_integration import get_modrinth_integration, ModrinthIntegration
from app.repositories.mod_repository import ModRepository
from app.repositories.mongo.mongo_mod_repository import MongoModRepository
from app.schemas.instance_schema import InstanceType
from app.schemas.mod_schema import ModSide, CompiledMod


class ModService:
    def __init__(self, repository: ModRepository, integrations: List[BaseIntegration]):
        self.repository = repository
        self.integrations = integrations

    async def get_compiled_mods(self, instance_type: InstanceType) -> List[CompiledMod]:
        mod_sides = ModSide.from_instance_type(instance_type)
        compiled_mods: List[CompiledMod] = []

        for integration in self.integrations:
            mods = await self.repository.get_by_integration_and_sides(integration.integration_type, mod_sides)
            compiled_mods.extend(await integration.get_mods(mods))

        return compiled_mods


IntegrationList = Sequence[BaseIntegration]


async def get_mod_service(repository: ModRepository = Depends(MongoModRepository),
                          modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
                          curseforge_integration: CurseforgeIntegration = Depends(
                              get_curseforge_integration)) -> ModService:
    integrations = [
        modrinth_integration,
        curseforge_integration
    ]
    return ModService(repository, integrations)
