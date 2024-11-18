from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.core.server import Server


def create_app(_=None) -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    return Server(app).get_app()
