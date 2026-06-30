"""Scrape several pages concurrently with the async client.

    pip install ghostcrawl
    export GHOSTCRAWL_API_KEY=gck_live_...
    python async_scrape.py

The GhostCrawl client is async, so a single client can fan out many scrapes
concurrently with asyncio.gather.
"""

import asyncio
import os

from ghostcrawl import GhostcrawlClient

URLS = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
]


async def main() -> None:
    async with GhostcrawlClient(api_key=os.environ["GHOSTCRAWL_API_KEY"]) as client:
        results = await asyncio.gather(
            *(client.scrape(url=url, engine="auto") for url in URLS)
        )
        for url, result in zip(URLS, results):
            print(url, "->", result["content"])


if __name__ == "__main__":
    asyncio.run(main())
