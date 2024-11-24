from app.repositories.instance_cache_repository import InstanceCacheRepository
from app.repositories.mongo.mongo_cache_repository import MongoCacheRepository


class MongoInstanceCacheRepository(InstanceCacheRepository, MongoCacheRepository):
    def __init__(self):
        super().__init__()
