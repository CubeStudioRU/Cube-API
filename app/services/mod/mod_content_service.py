from fastapi.params import Depends

from app.integrations.curseforge_integration import get_curseforge_integration, CurseforgeIntegration
from app.integrations.modrinth_integration import get_modrinth_integration, ModrinthIntegration
from app.repositories.mod.mod_content_repository import ModContentRepository
from app.repositories.repositories_mongo.mod.mongo_mod_content_repository import MongoModContentRepository
from app.services.content_service import ContentService


class ModContentService(ContentService):
    pass


async def get_mod_content_service(repository: ModContentRepository = Depends(MongoModContentRepository),
                                  modrinth_integration: ModrinthIntegration = Depends(get_modrinth_integration),
                                  curseforge_integration: CurseforgeIntegration = Depends(
                                      get_curseforge_integration)) -> ModContentService:
    integrations = [
        modrinth_integration,
        curseforge_integration
    ]
    return ModContentService(repository, integrations)
