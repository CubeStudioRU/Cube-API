from app.repositories.mod_cache_repository import ModCacheRepository
from app.repositories.mongo.mongo_cache_repository import MongoCacheRepository


class MongoModCacheRepository(ModCacheRepository, MongoCacheRepository):
    def __init__(self):
        super().__init__()
