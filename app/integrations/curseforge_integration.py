from typing import List

import aiohttp

from app.core.config import CURSEFORGE_API_KEY
from app.integrations.base_integration import BaseIntegration
from app.schemas.instance_schema import Instance
from app.schemas.mod_schema import CompiledInstanceMod, CurseforgeMod, BaseMod


class CurseforgeIntegration(BaseIntegration):
    BASE_URL = "https://api.curseforge.com/v1"
    API_KEY = CURSEFORGE_API_KEY

    async def get_mod(self, data: CurseforgeMod) -> CompiledInstanceMod:
        url = self.BASE_URL + f"/mods/{data.mod_id}/files/{data.file_id}"
        headers = {'Accept': 'application/json', 'x-api-key': self.API_KEY}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = (await response.json()).get("data")
                if not data:
                    raise Exception(f"{self.__repr__()} is empty")
                return CompiledInstanceMod(file=data.get("fileName"), url=data.get("downloadUrl"))

    async def extract_mods(self, instance: Instance) -> List[BaseMod]:
        return instance.curseforge


curseforge_integration = CurseforgeIntegration()
