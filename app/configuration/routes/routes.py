from dataclasses import dataclass
from fastapi import FastAPI

__all__ = ['Routes']

@dataclass(frozen=True)
class Routes:

    routers: tuple

    def register_routes(self, app: FastAPI):

        for router in self.routers:
            app.include_router(router)

