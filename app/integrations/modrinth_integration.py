from typing import List

import aiohttp
from fastapi.params import Depends

from app.integrations.base_integration import BaseIntegration
from app.schemas.content_schema import TypedContent, CompiledContent
from app.schemas.integration_schema import IntegrationType
from app.services.cache_service import CacheService
from app.services.mod_cache_service import ModCacheService, get_mod_cache_service


class ModrinthIntegration(BaseIntegration):
    BASE_URL = "https://api.modrinth.com/v2"

    async def get_content(self, content: TypedContent) -> CompiledContent:
        url = self.BASE_URL + f"/project/{content.project}/version/{content.version}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = await response.json()
                for file in data.get("files", []):
                    if file["primary"]:
                        return CompiledContent(file=file.get("filename"), url=file.get("url"))


async def get_modrinth_integration(
        mod_cache_service: ModCacheService = Depends(get_mod_cache_service)) -> ModrinthIntegration:
    cache_services: List[CacheService] = [
        mod_cache_service,
    ]
    return ModrinthIntegration(cache_services, IntegrationType.modrinth)
