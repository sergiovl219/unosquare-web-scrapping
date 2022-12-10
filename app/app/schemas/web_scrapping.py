from pydantic import BaseModel


class WebScrappingResponse(BaseModel):
    title_tag: str
    meta_description: str
    url_favicon: str
    body_first_h1: str
