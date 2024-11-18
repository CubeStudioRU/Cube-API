from fastapi import APIRouter

from app.compile import is_compiled_instance_up_to_date, get_compiled_instance, compile_instance
from app.objects import CompiledInstance

instances_router = APIRouter(
    prefix='/instances',
    tags=['Instances']
)


@instances_router.get('/')
async def get_instance() -> CompiledInstance:
    is_instance_compiled: bool = is_compiled_instance_up_to_date()
    if is_instance_compiled == None:
        return None

    if not is_instance_compiled:
        response = compile_instance()
        if not response:
            return None

    return get_compiled_instance()
