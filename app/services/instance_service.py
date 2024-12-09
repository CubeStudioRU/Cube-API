from fastapi.params import Depends

from app.repositories.instance.instance_repository import InstanceRepository
from app.repositories.repositories_mongo.instance.mongo_instance_repository import (
    MongoInstanceRepository,
)
from app.schemas.instance_schema import Instance


class InstanceService:
    def __init__(self, instance_repository: InstanceRepository):
        self.instance_repository = instance_repository

    async def create_instance(self, instance: Instance) -> None:
        return await self.instance_repository.save(instance)

    async def get_instance(self, instance_uuid: str = "0") -> Instance:
        instance = await self.instance_repository.get(instance_uuid)
        if instance:
            return instance

        instance = Instance(
            uuid="0",
            name="sample",
            version="1.0",
            changelog="placeholder",
            game_version="1.0",
            loader="sample",
            modrinth=[],
            curseforge=[],
        )
        await self.create_instance(instance)
        return instance


async def get_instance_service(
    instance_repository: InstanceRepository = Depends(MongoInstanceRepository),
) -> InstanceService:
    return InstanceService(instance_repository)
