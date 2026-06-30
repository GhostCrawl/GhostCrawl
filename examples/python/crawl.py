"""Start a crawl run and read its status.

    pip install ghostcrawl
    export GHOSTCRAWL_API_KEY=gck_live_...
    python crawl.py

The Python SDK is async — call it from inside an async function.
"""

import asyncio
import os

from ghostcrawl import GhostcrawlClient


async def main() -> None:
    async with GhostcrawlClient(api_key=os.environ["GHOSTCRAWL_API_KEY"]) as client:
        run = await client.crawl_runs.start(
            url="https://example.com",
            max_depth=2,
            max_pages=25,
        )
        run_id = run["run_id"]
        print("run id:", run_id)

        # Fetch the run's current status.
        status = await client.crawl_runs.get(run_id)
        print("status:", status)


if __name__ == "__main__":
    asyncio.run(main())
