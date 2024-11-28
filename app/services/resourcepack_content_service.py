from fastapi.params import Depends

from app.integrations.curseforge_integration import get_curseforge_integration, CurseforgeIntegration
from app.integrations.modrinth_integration import get_modrinth_integration, ModrinthIntegration
from app.repositories.mongo.mongo_resourcepack_content_repository import MongoResourcepackContentRepository
from app.repositories.resourcepack_content_repository import ResourcepackContentRepository
from app.services.content_service import ContentService


class ResourcepackContentService(ContentService):
    pass


async def get_resourcepack_content_service(
        repository: ResourcepackContentRepository = Depends(MongoResourcepackContentRepository),
        modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
        curseforge_integration: CurseforgeIntegration = Depends(
            get_curseforge_integration)) -> ResourcepackContentService:
    integrations = [
        modrinth_integration,
        curseforge_integration
    ]
    return ResourcepackContentService(repository, integrations)