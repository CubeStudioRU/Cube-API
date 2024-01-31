from fastapi import FastAPI
from app.configuration.routes import __routes__

class Server:

    __app: FastAPI


    def __init__(self, app: FastAPI) -> None:
        self.__app = app
        self.__register_routes(app)


    def get_app(self) -> FastAPI:
        return self.__app
    
    @staticmethod
    def __register_events(app):

        ...

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)
    