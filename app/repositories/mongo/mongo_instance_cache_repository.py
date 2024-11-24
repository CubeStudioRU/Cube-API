from app.repositories.instance_cache_repository import InstanceCacheRepository
from app.repositories.mongo.mongo_cache_repository import MongoCacheRepository
from app.schemas.instance_schema import CachedInstance


class MongoInstanceCacheRepository(MongoCacheRepository, InstanceCacheRepository):
    entity_model = CachedInstance
