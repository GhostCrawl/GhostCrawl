"""Scrape a single page with the GhostCrawl Python SDK.

    pip install ghostcrawl
    export GHOSTCRAWL_API_KEY=gck_live_...
    python scrape.py

The Python SDK is async — call it from inside an async function.
"""

import asyncio
import os

from ghostcrawl import GhostcrawlClient


async def main() -> None:
    async with GhostcrawlClient(api_key=os.environ["GHOSTCRAWL_API_KEY"]) as client:
        result = await client.scrape(url="https://example.com", engine="chrome")
        print(result["content"])


if __name__ == "__main__":
    asyncio.run(main())
