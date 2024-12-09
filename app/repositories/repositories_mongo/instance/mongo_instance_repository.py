from app.repositories.instance.instance_repository import InstanceRepository
from app.repositories.repositories_mongo.mongo_base_repository import (
    MongoBaseRepository,
)
from app.schemas.instance_schema import Instance


class MongoInstanceRepository(MongoBaseRepository[Instance], InstanceRepository):
    entity_model = Instance
