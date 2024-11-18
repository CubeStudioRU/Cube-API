from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan():
    yield
