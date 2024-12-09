from fastapi import Depends

from app.integrations.base_integration import BaseIntegration
from app.integrations.integrations_dependency import get_integrations
from app.repositories.repositories_mongo.resourcepack.mongo_resourcepack_content_repository import (
    MongoResourcepackContentRepository,
)
from app.repositories.resourcepack.resourcepack_content_repository import (
    ResourcepackContentRepository,
)
from app.services.content_service import ContentService


class ResourcepackContentService(ContentService):
    pass


async def get_resourcepack_content_service(
    repository: ResourcepackContentRepository = Depends(MongoResourcepackContentRepository),
    integrations: list[BaseIntegration] = Depends(get_integrations),
) -> ResourcepackContentService:
    return ResourcepackContentService(repository, integrations)
