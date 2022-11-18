from typing import Union

from fastapi import APIRouter

from ....schemas import WebScrappingResponse

router = APIRouter()


@router.get(
    "/",
    response_model=WebScrappingResponse
)
def web_info(
        url: str,
):

    return {
        "title_tag": url,
        "meta_description": url,
        "url_favicon": url,
        "body_first_h1": url,
    }
