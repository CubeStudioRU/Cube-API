from app.repositories.mod.mod_content_repository import ModContentRepository
from app.repositories.repositories_mongo.mongo_content_repository import (
    MongoContentRepository,
)
from app.schemas.mod_content_schema import TypedModContent


class MongoModContentRepository(MongoContentRepository, ModContentRepository):
    entity_model = TypedModContent
