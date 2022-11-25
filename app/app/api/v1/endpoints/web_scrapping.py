from urllib.parse import urlparse
from urllib.parse import urlunparse

import requests

from bs4 import BeautifulSoup
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
    """
    Endpoint to get the following info for a website: title tag info, meta description content,
    favicon url and the first h1 tag from body.

    Args:
        url: The URL from where we will obtain the information

    Returns:
        dict with the information obtained from the URL.
    """
    page = requests.get(url)
    domain = urlparse(url).netloc

    soup = BeautifulSoup(page.content, "html.parser")

    # TODO: Business logic in another file?
    title = soup.find('title')
    title_tag = title.string if title else "No title content given"

    meta_description = soup.find("meta", property="og:description")
    meta_description_content = meta_description["content"] if meta_description else "No meta description given"

    links = soup.find_all(name='link') or []
    icons = [e for e in links if 'icon' in str(e.attrs.get('rel'))]

    url_favicon = "No favicon given"
    if icons:
        href_favicon = icons[0].attrs.get('href')
        url_favicon = urlparse(href_favicon, scheme='http')
        if not url_favicon.netloc:
             url_favicon = urlunparse((url_favicon.scheme, domain, url_favicon.path, '', '', ''))
        else:
            url_favicon = url_favicon.geturl()

    page_body = soup.find('body')
    if page_body:
        first_h1 = page_body.find_next("h1")
        string_first_h1 = first_h1.string if first_h1 else "No h1 tags given in body"
        body_first_h1 = string_first_h1 or "No h1 text given"
    else:
        body_first_h1 = "No body given"

    return {
        "title_tag": title_tag,
        "meta_description": meta_description_content,
        "url_favicon": url_favicon,
        "body_first_h1": body_first_h1,
    }
