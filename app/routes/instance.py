from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1'
)

@router.get('/hello')
async def hello():
    return {
        'hello':'world'
    }