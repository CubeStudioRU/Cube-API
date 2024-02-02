from fastapi import APIRouter
from app.objects import Instance
import json

router = APIRouter(
    prefix='/api/v1'
)

@router.get('/hello')
async def hello():
    return {
        'hello':'world'
    }