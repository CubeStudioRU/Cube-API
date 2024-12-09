from typing import List

from fastapi.params import Depends

from app.integrations.base_integration import BaseIntegration
from app.integrations.integrations_dependency import get_integrations
from app.repositories.mod.mod_content_repository import ModContentRepository
from app.repositories.repositories_mongo.mod.mongo_mod_content_repository import MongoModContentRepository
from app.services.content_service import ContentService


class ModContentService(ContentService):
    pass


async def get_mod_content_service(
        repository: ModContentRepository = Depends(MongoModContentRepository),
        integrations: List[BaseIntegration] = Depends(get_integrations),
) -> ModContentService:
    return ModContentService(repository, integrations)
