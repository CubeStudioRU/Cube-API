from abc import ABC
from typing import List

from app.repositories.base_repository import BaseRepository
from app.schemas.mod_schema import IntegrationMod, IntegrationType, ModSide


class ModRepository(BaseRepository[IntegrationMod], ABC):
    repository_name = "mods"

    def get_by_integration_and_sides(self, integration_type: IntegrationType, mod_sides: List[ModSide]) -> List[
        IntegrationMod]:
        pass
