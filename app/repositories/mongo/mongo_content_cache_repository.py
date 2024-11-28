from app.repositories.content_cache_repository import ContentCacheRepository
from app.repositories.mongo.mongo_cache_repository import MongoCacheRepository


class MongoContentCacheRepository(MongoCacheRepository, ContentCacheRepository):
    pass
