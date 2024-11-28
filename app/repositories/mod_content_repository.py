from abc import ABC

from app.repositories.content_repository import ContentRepository


class ModContentRepository(ContentRepository, ABC):
    repository_name = "mods"
