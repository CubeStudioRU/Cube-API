from abc import ABC

from app.repositories.content_repository import ContentRepository


class ResourcepackContentRepository(ContentRepository, ABC):
    repository_name = "resourcepacks"
