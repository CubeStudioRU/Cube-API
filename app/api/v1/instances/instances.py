from fastapi import APIRouter

from app.schemas.instance_schema import CompiledInstance
from app.services.compile_service import CompileService

instances_router = APIRouter(
    prefix='/instances',
    tags=['Instances']
)


@instances_router.get('/')
async def get_instance() -> CompiledInstance:
    return await CompileService.get_compiled_instance()
