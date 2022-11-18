from fastapi import APIRouter

from app.api.v1.endpoints import test
from app.api.v1.endpoints import web_scrapping

api_router = APIRouter()
api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"]
)
api_router.include_router(
    web_scrapping.router,
    prefix="/web-scrapping",
    tags=["web-scrapping"]
)
