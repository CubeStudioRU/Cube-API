from app.repositories.mod_cache_repository import ModCacheRepository
from app.repositories.mongo.mongo_cache_repository import MongoCacheRepository
from app.schemas.mod_schema import CachedMod


class MongoModCacheRepository(MongoCacheRepository, ModCacheRepository):
    entity_model = CachedMod
