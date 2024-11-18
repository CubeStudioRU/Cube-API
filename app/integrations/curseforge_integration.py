import aiohttp

from app.core.config import BASE_CURSEFORGE_URL, CURSEFORGE_API_KEY
from app.integrations.base_integration import BaseIntegration
from app.schemas import CompiledInstanceMod


class CurseforgeIntegration(BaseIntegration):
    BASE_URL = BASE_CURSEFORGE_URL
    API_KEY = CURSEFORGE_API_KEY

    async def get_mod(self, mod_id: str, file_id: str) -> CompiledInstanceMod:
        url = self.BASE_URL + f"/mods/{mod_id}/files/{file_id}"
        headers = {'Accept': 'application/json', 'x-api-key': self.API_KEY}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    raise Exception(f"{self.__repr__()} is not reachable")
                data = (await response.json()).get("data")
                if not data:
                    raise Exception(f"{self.__repr__()} is empty")
                return CompiledInstanceMod(file=data.get("fileName"), url=data.get("downloadUrl"))
