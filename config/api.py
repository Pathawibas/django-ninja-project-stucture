from ninja import NinjaAPI, Swagger, Redoc
from apps.core.api import router as core_router


api = NinjaAPI()

# https://django-ninja.dev/guides/routers/
api.add_router("", core_router)
