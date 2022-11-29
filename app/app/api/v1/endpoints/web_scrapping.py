from urllib.parse import urlparse
from urllib.parse import urlunparse

import requests

from bs4 import BeautifulSoup
from fastapi import APIRouter

from ....schemas import WebScrappingResponse
from ....services.web_scrapping import WebScrappingService

router = APIRouter()


@router.get(
    "/",
    response_model=WebScrappingResponse
)
def web_info(
        url: str,
):
    """
    Endpoint to get the following info for a website: title tag info, meta description content,
    favicon url and the first h1 tag from body.

    Args:
        :param url: The URL from where we will obtain the information

    Returns:
        dict with the information obtained from the URL.
    """
    web_scrapping_service = WebScrappingService(url=url)

    return web_scrapping_service.get_web_scrapping_response()
