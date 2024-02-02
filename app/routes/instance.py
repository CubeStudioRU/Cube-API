from fastapi import APIRouter
from app.compile import is_compiled_instance_up_to_date, get_compiled_instance, compile_instance
from app.objects import CompiledInstance

router = APIRouter(
    prefix='/api/v1'
)

@router.get('/get_compiled_instance')
async def get_compiled_instance_api() -> CompiledInstance:
    is_instance_compiled: bool = is_compiled_instance_up_to_date()
    if is_instance_compiled == None:
        return None
    
    if not is_instance_compiled:
        response = compile_instance()
        if not response:
            return None

    return get_compiled_instance()