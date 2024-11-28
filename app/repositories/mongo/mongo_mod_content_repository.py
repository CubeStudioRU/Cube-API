from app.repositories.mod_content_repository import ModContentRepository
from app.repositories.mongo.mongo_content_repository import MongoContentRepository
from app.schemas.mod_schema import IntegrationMod


class MongoModContentRepository(MongoContentRepository, ModContentRepository):
    entity_model = IntegrationMod
