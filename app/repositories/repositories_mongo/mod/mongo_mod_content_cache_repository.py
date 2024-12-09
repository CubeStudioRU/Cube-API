from app.repositories.mod.mod_content_cache_repository import ModContentCacheRepository
from app.repositories.repositories_mongo.mongo_content_cache_repository import (
    MongoContentCacheRepository,
)
from app.schemas.mod_content_schema import ModCachedContent


class MongoModContentCacheRepository(MongoContentCacheRepository, ModContentCacheRepository):
    entity_model = ModCachedContent
