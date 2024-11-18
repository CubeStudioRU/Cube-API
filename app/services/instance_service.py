from app.core.config import INSTANCE_FILE
from app.crud.files import get_json
from app.schemas.instance_schema import Instance


class InstanceService:
    def __init__(self):
        pass

    async def get_instance(self) -> Instance:
        return Instance.model_validate(get_json(INSTANCE_FILE))


async def instance_service_factory() -> InstanceService:
    return InstanceService()
