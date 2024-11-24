from enum import Enum
from typing import Optional, Mapping, Any, List

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.core.config import get_settings, get_mongo_settings


class CollectionsEnum(str, Enum):
    INSTANCES = "instances"
    MODS_CACHE = "mods_cache"
    INSTANCES_CACHE = "instances_cache"


class AsyncMongoStorage:
    def __init__(self):
        mongo_settings = get_mongo_settings()
        self.mongo_uri = mongo_settings.MONGO_URI
        self.database_name = get_settings().PROJECT_NAME
        self._connection: Optional[AsyncIOMotorClient] = None

    async def connect(self) -> None:
        self._connection = AsyncIOMotorClient(self.mongo_uri)

    async def disconnect(self) -> None:
        if self._connection:
            self._connection.close()
            self._connection = None

    async def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        if not self._connection:
            raise RuntimeError("MongoDB connection is not initialized.")
        db = self._connection.get_database(self.database_name)
        return db.get_collection(collection_name)

    async def find_one(self, collection_name: str, filter: dict) -> Optional[Mapping[str, Any]]:
        collection = await self.get_collection(collection_name)
        return await collection.find_one(filter)

    async def find_all(self, collection_name: str, filter: dict = {}) -> List[Mapping[str, Any]]:
        collection = await self.get_collection(collection_name)
        cursor = collection.find(filter)
        return await cursor.to_list(length=None)

    async def insert_one(self, collection_name: str, document: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.insert_one(document)

    async def insert_many(self, collection_name: str, documents: List[dict]) -> None:
        collection = await self.get_collection(collection_name)
        await collection.insert_many(documents)

    async def update_one(self, collection_name: str, filter: dict, update: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.update_one(filter, {"$set": update})

    async def delete_one(self, collection_name: str, filter: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.delete_one(filter)

    async def delete_many(self, collection_name: str, filter: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.delete_many(filter)
