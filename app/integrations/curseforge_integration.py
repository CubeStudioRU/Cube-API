from typing import List

import aiohttp

from app.core.config import get_settings
from app.integrations.base_integration import BaseIntegration
from app.schemas.instance_schema import Instance
from app.schemas.mod_schema import CurseforgeMod, CompiledMod, IntegrationMod


class CurseforgeIntegration(BaseIntegration):
    BASE_URL = "https://api.curseforge.com/v1"
    API_KEY = get_settings().curseforge_api_key

    async def get_mod(self, data: CurseforgeMod) -> CompiledMod:
        url = self.BASE_URL + f"/mods/{data.mod_id}/files/{data.file_id}"
        headers = {'Accept': 'application/json', 'x-api-key': self.API_KEY}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = (await response.json()).get("data")
                if not data:
                    raise Exception(f"{self.__repr__()} is empty")
                return CompiledMod(file=data.get("fileName"), url=data.get("downloadUrl"))

    async def extract_mods(self, instance: Instance) -> List[IntegrationMod]:
        return instance.curseforge


curseforge_integration = CurseforgeIntegration()
