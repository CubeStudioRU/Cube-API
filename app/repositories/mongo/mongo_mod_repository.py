from typing import List, Optional

from app.repositories.mod_repository import ModRepository
from app.repositories.mongo.mongo_base_repository import MongoBaseRepository, Entity
from app.schemas.mod_schema import IntegrationMod, IntegrationType, ModSide


class MongoModRepository(MongoBaseRepository[IntegrationMod], ModRepository):
    entity_model = IntegrationMod

    async def get(self, entity_uuid: str) -> Optional[Entity]:
        return None

    async def get_by_integration(self, integration: IntegrationType) -> List[entity_model]:
        documents = await self.storage.find_all(self.repository_name, {"integration": integration.name})
        return [self.entity_model.model_validate(document) for document in documents]

    async def get_by_sides(self, sides: List[ModSide]) -> List[entity_model]:
        documents = await self.storage.find_all(self.repository_name, {"side": {"$in": sides}})
        return [self.entity_model.model_validate(document) for document in documents]

    async def get_by_integration_and_sides(self, integration: IntegrationType, sides: List[ModSide]) -> List[
        entity_model]:
        documents = await self.storage.find_all(self.repository_name,
                                                {"integration": integration.name, "side": {"$in": sides}})
        return [self.entity_model.model_validate(document) for document in documents]
