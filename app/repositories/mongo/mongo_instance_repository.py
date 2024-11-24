from app.repositories.instance_repository import InstanceRepository
from app.repositories.mongo.mongo_base_repository import MongoBaseRepository


class MongoInstanceRepository(InstanceRepository, MongoBaseRepository):
    def __init__(self):
        super().__init__()
