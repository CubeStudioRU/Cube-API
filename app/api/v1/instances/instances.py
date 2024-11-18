from fastapi import APIRouter

from app.compile import is_compiled_instance_up_to_date, get_compiled_instance, compile_instance
from app.schemas import CompiledInstance

instances_router = APIRouter(
    prefix='/instances',
    tags=['Instances']
)


@instances_router.get('/')
async def get_instance() -> CompiledInstance:
    is_instance_compiled: bool = await is_compiled_instance_up_to_date()
    if is_instance_compiled is None:
        return None

    if not is_instance_compiled:
        response = await compile_instance()
        if not response:
            return None

    return await get_compiled_instance()
