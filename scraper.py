"""
Given a website URL, scrape all HTML in the website in a tree.
Async scraper is needed in Gradio.
Ref: https://stackoverflow.com/questions/42009202/how-to-call-a-async-function-contained-in-a-class
"""
import asyncio
from urllib.parse import urlparse
from playwright.async_api import async_playwright
import re

from init import *


def url2name(url):
    tokens = re.split(r'[/:?#.@$%\\*]', url)
    return '.'.join([t for t in tokens if t != ''])


class Scraper:
    def __init__(self, dir="data/tmp"):
        self.dir = init_dir(dir)
        self.links = {}

    async def scrape_url(self, url):
        await self.page.goto(url)
        html_content = await self.page.content()
        filename = url2name(url)
        with open(f"{self.dir}/{filename}.html", 'w') as f:
            f.write(html_content)

        hrefs = set(await self.page.eval_on_selector_all("a", "e => e.map(e => e.href)"))
        urls = [urlparse(href)._replace(query="", fragment="") for href in hrefs]
        urls = filter(lambda url: url.netloc == self.domain, urls)  # internal links
        urls = filter(lambda url: url.scheme == "https", urls)  # not mailto
        urls = list(set([url.geturl() for url in urls]))
        self.links[url] = urls

    async def async_scrape(self, url, depth=2):
        scheme = urlparse(url).scheme
        assert scheme == "https" or scheme == "http", f"URL must begin with 'https' or 'http': {url}"
        url = urlparse(url)._replace(query="", fragment="")
        self.domain = url.netloc
        url = url.geturl()

        print("Initializing scraper.")
        async with async_playwright() as playwright:
            chromium = playwright.chromium
            browser = await chromium.launch()
            self.page = await browser.new_page()
            print("Scraper initialized.")

            print("Scraping:", url)
            await self.scrape_url(url)
            urls = self.links[url]

            for d in range(depth):
                print(f"\nScraping depth: {d+1} - Found {len(urls)} links.")
                next_urls = []
                for i, url in enumerate(urls):
                    print(f"{i+1}.", url)
                    await self.scrape_url(url)
                for url in urls:
                    for next_url in self.links[url]:
                        if next_url not in self.links and next_url not in next_urls:
                            next_urls.append(next_url)
                urls = next_urls

    def scrape(self, url, depth=2):
        asyncio.run(self.async_scrape(url, depth))


if __name__ == "__main__":
    scraper = Scraper(dir="data")
    scraper.scrape("https://example.com/", depth=1)
