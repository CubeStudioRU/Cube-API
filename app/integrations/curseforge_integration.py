import aiohttp
from fastapi.params import Depends

from app.core.config import get_settings
from app.integrations.base_integration import BaseIntegration
from app.schemas.mod_schema import IntegrationMod, CompiledMod, IntegrationType
from app.services.mod_cache_service import ModCacheService, get_mod_cache_service


class CurseforgeIntegration(BaseIntegration):
    BASE_URL = "https://api.curseforge.com/v1"
    API_KEY = get_settings().curseforge_api_key

    async def get_mod(self, mod: IntegrationMod) -> CompiledMod:
        url = self.BASE_URL + f"/mods/{mod.mod}/files/{mod.version}"
        headers = {'Accept': 'application/json', 'x-api-key': self.API_KEY}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = (await response.json()).get("data")
                if not data:
                    raise Exception(f"{self.__repr__()} is empty")
                return CompiledMod(file=data.get("fileName"), url=data.get("downloadUrl"))


async def get_curseforge_integration(
        mod_cache_service: ModCacheService = Depends(get_mod_cache_service)) -> CurseforgeIntegration:
    return CurseforgeIntegration(mod_cache_service, IntegrationType.curseforge)
