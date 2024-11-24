from abc import ABC

from app.repositories.base_repository import BaseRepository
from app.schemas.instance_schema import Instance


class InstanceRepository(BaseRepository[Instance], ABC):
    repository_name = "instances"
