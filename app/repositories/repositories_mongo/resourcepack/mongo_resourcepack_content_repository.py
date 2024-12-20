from app.repositories.repositories_mongo.mongo_content_repository import (
    MongoContentRepository,
)
from app.repositories.resourcepack.resourcepack_content_repository import (
    ResourcepackContentRepository,
)
from app.schemas.resourcepack_content_schema import TypedResourcepackContent


class MongoResourcepackContentRepository(MongoContentRepository, ResourcepackContentRepository):
    entity_model = TypedResourcepackContent
