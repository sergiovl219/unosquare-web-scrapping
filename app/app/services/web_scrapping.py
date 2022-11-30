from urllib.parse import urlparse
from urllib.parse import urlunparse

import requests
from bs4 import BeautifulSoup

from app.services.main import AppService


class WebScrappingService(AppService):
    def __init__(self, url: str):
        """
        Object initialization with the url to perform the web scrapping.
        BeautifulSoup and Request are used to get the objects that will be shared in the methods.

        Args:
         :param url: The URL from where we will obtain the information.
        """
        super().__init__()
        page = requests.get(url)
        self.soup = BeautifulSoup(page.content, "html.parser")
        self.url = url

    def get_title_tag_content(self) -> str:
        """
        Method to get the title tag content from a website.

        Returns:
            Tittle tag content text or default text response.
        """
        title = self.soup.find('title')
        title_tag = title.string if title else "No title content given"
        return title_tag

    def get_meta_description_content(self) -> str:
        """
        Method to get the meta description content from a website.

        Returns:
            Meta description content text or default text response.
        """
        meta_description = self.soup.find("meta", property="og:description")
        meta_description_content = meta_description["content"] if meta_description else "No meta description given"
        return meta_description_content

    def get_url_favicon(self) -> str:
        """
        Method to get the URL of the favicon website.

        Returns:
            Tittle tag content text or default text response.
        """
        domain = urlparse(self.url).netloc

        links = self.soup.find_all(name='link') or []
        icons = [e for e in links if 'icon' in str(e.attrs.get('rel'))]

        url_favicon = "No favicon given"
        if icons:
            href_favicon = icons[0].attrs.get('href')
            url_favicon = urlparse(href_favicon, scheme='http')
            if not url_favicon.netloc:
                url_favicon = urlunparse((url_favicon.scheme, domain, url_favicon.path, '', '', ''))
            else:
                url_favicon = url_favicon.geturl()
        return url_favicon

    def get_body_first_h1(self) -> str:
        """
        Method to get the first h1 tag content from a website.

        Returns:
            First h1 tag content text or default text response.
        """
        page_body = self.soup.find('body')
        if page_body:
            first_h1 = page_body.find_next("h1")
            string_first_h1 = first_h1.string if first_h1 else "No h1 tags given in body"
            body_first_h1 = string_first_h1 or "No h1 text given"
        else:
            body_first_h1 = "No body given"
        return body_first_h1

    def get_web_scrapping_response(self) -> dict:
        """
        Method to map the response for the web-scrapping endpoint.

        Returns:
            Dictionary, mapping all the required fields in WebScrappingResponse schema.
        """
        return {
            "title_tag": self.get_title_tag_content(),
            "meta_description": self.get_meta_description_content(),
            "url_favicon": self.get_url_favicon(),
            "body_first_h1": self.get_body_first_h1(),
        }
