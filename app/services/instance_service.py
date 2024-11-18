from app.core.config import INSTANCE_FILE
from app.crud.files import get_json
from app.schemas.instance_schema import Instance


class InstanceService:
    @staticmethod
    async def get_instance() -> Instance:
        return Instance.model_validate(get_json(INSTANCE_FILE))
