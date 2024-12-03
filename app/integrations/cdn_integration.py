from typing import List

from fastapi import Depends

from app.integrations.base_integration import BaseIntegration
from app.schemas.content_schema import TypedContent, CompiledContent
from app.schemas.integration_schema import IntegrationType
from app.services.cache_service import CacheService
from app.services.mod.mod_content_cache_service import ModContentCacheService, get_mod_cache_service
from app.services.resourcepack.resourcepack_content_cache_service import ResourcepackContentCacheService, \
    get_resourcepack_content_cache_service


class CdnIntegration(BaseIntegration):
    BASE_URL = ""

    async def get_content(self, content: TypedContent) -> CompiledContent:
        return CompiledContent(url=content.project, file=content.version)


async def get_cdn_integration(
        mod_content_cache_service: ModContentCacheService = Depends(get_mod_cache_service),
        resourcepack_content_cache_service: ResourcepackContentCacheService = Depends(
            get_resourcepack_content_cache_service)) -> CdnIntegration:
    cache_services: List[CacheService] = [
        mod_content_cache_service,
        resourcepack_content_cache_service,
    ]
    return CdnIntegration(cache_services, IntegrationType.cdn)
