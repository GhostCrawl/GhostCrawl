"""Extract structured JSON from a page against a schema.

    pip install ghostcrawl
    export GHOSTCRAWL_API_KEY=gck_live_...
    python extract.py

The Python SDK is async — call it from inside an async function.
"""

import asyncio
import os

from ghostcrawl import GhostcrawlClient


async def main() -> None:
    async with GhostcrawlClient(api_key=os.environ["GHOSTCRAWL_API_KEY"]) as client:
        result = await client.extract(
            url="https://example.com",
            schema={
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "summary": {"type": "string"},
                },
            },
        )
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
