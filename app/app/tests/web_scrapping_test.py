import pytest
from fastapi.testclient import TestClient

from app.core.config import settings

from ..main import app

client = TestClient(app)


def test_web_info() -> None:
    """

    """
    data = {"title": "Foo", "description": "Fighters"}
    # Test OK, all keys given and all data filled.
    response = client.get(
        f"{settings.API_V1_STR}/web-scrapping/",
        params={"url": "https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html"}
    )
    assert response.status_code == 200
    content = response.json()

    # Test all keys expected in response.
    assert content.get("title_tag")
    assert content.get("meta_description")
    assert content.get("url_favicon")
    assert content.get("body_first_h1")

    # Test all data filled in response.
    assert content.get("title_tag") is not None
    assert content.get("meta_description") is not None
    assert content.get("url_favicon") is not None
    assert content.get("body_first_h1") is not None
