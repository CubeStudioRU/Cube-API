from app.repositories.mod_content_cache_repository import ModContentCacheRepository
from app.repositories.mongo.mongo_content_cache_repository import MongoContentCacheRepository
from app.schemas.mod_schema import CachedMod


class MongoModContentCacheRepository(MongoContentCacheRepository, ModContentCacheRepository):
    entity_model = CachedMod
