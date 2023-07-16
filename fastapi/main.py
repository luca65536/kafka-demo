from api.routes import router
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Import and include the API routes
app.include_router(router)


def custom_openapi():
    """
        Swagger set up.


        Basic Swagger configuration for initial api documentation.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Kafka Demo FastAPI",
        version="1.0.0",
        description="This is a fancy API using FastAPI",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
