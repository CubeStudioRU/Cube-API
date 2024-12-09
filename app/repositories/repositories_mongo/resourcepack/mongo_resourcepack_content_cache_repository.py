from app.repositories.repositories_mongo.mongo_content_cache_repository import (
    MongoContentCacheRepository,
)
from app.repositories.resourcepack.resourcepack_content_cache_repository import (
    ResourcepackContentCacheRepository,
)
from app.schemas.resourcepack_content_schema import ResourcepackCachedContent


class MongoResourcepackContentCacheRepository(MongoContentCacheRepository, ResourcepackContentCacheRepository):
    entity_model = ResourcepackCachedContent
