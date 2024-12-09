from fastapi import APIRouter

from .instances.instances import instances_router

subrouters = (instances_router,)

v1_router = APIRouter(prefix="/v1")

for subrouter in subrouters:
    v1_router.include_router(subrouter)
