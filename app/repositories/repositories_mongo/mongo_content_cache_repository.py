from app.repositories.content_cache_repository import ContentCacheRepository
from app.repositories.repositories_mongo.mongo_cache_repository import (
    MongoCacheRepository,
)


class MongoContentCacheRepository(MongoCacheRepository, ContentCacheRepository):
    pass
