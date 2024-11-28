from app.repositories.mod_content_repository import ModContentRepository
from app.repositories.mongo.mongo_content_repository import MongoContentRepository
from app.schemas.mod_content_schema import TypedModContent


class MongoModContentRepository(MongoContentRepository, ModContentRepository):
    entity_model = TypedModContent
