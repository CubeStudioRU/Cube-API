from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.instance_schema import InstanceType
from app.services.compile_service import CompileService, get_compile_service

instances_router = APIRouter(
    prefix='/instances',
    tags=['Instances']
)


@instances_router.get('/')
async def get_instance(instance_type: InstanceType = InstanceType.client,
                       compile_service: CompileService = Depends(get_compile_service)):
    compiled_instance = await compile_service.get_compiled_instance(instance_type)
    return compiled_instance
