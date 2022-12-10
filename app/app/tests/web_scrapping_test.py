from app.core.config import settings
from fastapi.testclient import TestClient


def test_web_info_keys_validation(
    client: TestClient
) -> None:
    """
    Test OK, response status 200 and all keys given in response.
    """
    response = client.get(
        f"{settings.API_V1_STR}/web-scrapping/",
        params={
            "url": "https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html"
        }
    )
    assert response.status_code == 200
    content = response.json()

    # Test all keys expected in response.
    assert content.get("title_tag")
    assert content.get("meta_description")
    assert content.get("url_favicon")
    assert content.get("body_first_h1")


def test_web_info_keys_validation_data_filled(
        client: TestClient
) -> None:
    """
    Test OK, response status 200 and all keys given and all data filled.
    """
    response = client.get(
        f"{settings.API_V1_STR}/web-scrapping/",
        params={
            "url": "https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html"
        }
    )
    assert response.status_code == 200
    content = response.json()

    # Test all data filled in response.
    assert content.get("title_tag") is not None
    assert content.get("meta_description") is not None
    assert content.get("url_favicon") is not None
    assert content.get("body_first_h1") is not None


def test_web_info_no_meta_description_content(
        client: TestClient
) -> None:
    """
    Test OK, response status 200 and all keys given but no meta description in website.
    """
    response = client.get(
        f"{settings.API_V1_STR}/web-scrapping/",
        params={
            "url": "https://python-poetry.org/"
        }
    )
    assert response.status_code == 200
    content = response.json()

    # Test all data filled in response.
    assert content.get("title_tag") is not None
    assert content.get("meta_description") == "No meta description given"
    assert content.get("url_favicon") is not None
    assert content.get("body_first_h1") is not None


def test_web_info_no_body_first_h1(
        client: TestClient
) -> None:
    """
    Test OK, response status 200 and all keys given but no h1 tag in body's website.
    """
    response = client.get(
        f"{settings.API_V1_STR}/web-scrapping/",
        params={
            "url": "https://python-poetry.org/"
        }
    )
    assert response.status_code == 200
    content = response.json()

    # Test all data filled in response.
    assert content.get("title_tag") is not None
    assert content.get("meta_description") is not None
    assert content.get("url_favicon") is not None
    assert content.get("body_first_h1") == "No h1 text given"
