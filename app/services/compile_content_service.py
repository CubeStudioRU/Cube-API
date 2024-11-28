from typing import List

from fastapi.params import Depends

from app.schemas.content_schema import CompiledContentContainer
from app.schemas.instance_schema import InstanceType
from app.services.content_service import ContentService
from app.services.mod_content_service import ModContentService, get_mod_content_service
from app.services.resourcepack_content_service import ResourcepackContentService, get_resourcepack_content_service


class CompileContentService:
    def __init__(self, content_services: List[ContentService]):
        self.content_services = content_services

    async def get_compiled_contents(self, instance_type: InstanceType) -> List[CompiledContentContainer]:
        compiled_contents = []
        for content_service in self.content_services:
            compiled_content = await content_service.get_compiled_contents(instance_type)
            compiled_content_container = CompiledContentContainer(content=compiled_content,
                                                                  content_type=content_service.repository.repository_name)
            compiled_contents.append(compiled_content_container)

        return compiled_contents

    async def get_contents_hash(self) -> str:
        hash = ""
        for content_service in self.content_services:
            hash += await content_service.get_contents_hash()
        return hash


async def get_compile_content_service(
        mod_content_service: ModContentService = Depends(get_mod_content_service),
        resourcepack_content_service: ResourcepackContentService = Depends(
            get_resourcepack_content_service)) -> CompileContentService:
    content_services: List[ContentService] = [
        mod_content_service,
        resourcepack_content_service,
    ]
    return CompileContentService(content_services)
