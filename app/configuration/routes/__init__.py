from app.configuration.routes.routes import Routes
from app.routes import instance

__routes__ = Routes(routers=(instance.router, ))