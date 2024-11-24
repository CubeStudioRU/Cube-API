from app.repositories.instance_repository import InstanceRepository
from app.repositories.mongo.mongo_base_repository import MongoBaseRepository
from app.schemas.instance_schema import Instance


class MongoInstanceRepository(MongoBaseRepository[Instance], InstanceRepository):
    entity_model = Instance
