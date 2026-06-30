# Self-host usage

Run the Docker image on your own machine. Your compute, your IP, your data.

A self-hosted instance runs the browser engines locally and exposes its own MCP,
REST API, and dashboard. It is not the managed cloud control plane — it is you
managing your own local instance, including watching and driving live sessions on
your own hardware.

---

## Bring it up

```bash
cp docker-compose.yml.template docker-compose.yml
echo "GHOSTCRAWL_API_KEY=gck_live_..." > .env   # in the same directory
docker compose up -d                            # launch locally
docker compose logs -f                          # follow the logs
```

The image is published at `ghcr.io/ghostcrawl/ghostcrawl`. Your API key is read
from the `.env` file beside the compose file and is validated online each time
the container starts.

---

## Online-required start

The self-host image validates your API key online **every time it starts**.
There is no offline grace period: if the cloud license check fails or the API is
unreachable, startup aborts. Keep outbound access to the ghostcrawl API open on
the host.

---

## Local endpoints

A running instance exposes three local surfaces:

| Surface | Default | Purpose |
|---------|---------|---------|
| REST API | `http://localhost:8000` | Same SDK surface as the cloud, pointed at your local instance. |
| MCP | `http://localhost:3143` | Drive the local browsers from an agent. |
| Dashboard | local web UI | Manage your instance, watch and control live sessions. |

Point an SDK at your local instance by overriding the base URL:

```python
import asyncio
from ghostcrawl import GhostcrawlClient

async def main():
    async with GhostcrawlClient(api_key="gck_live_...", base_url="http://localhost:8000") as client:
        result = await client.scrape(url="https://example.com")
        print(result["content"])

asyncio.run(main())
```

Live browser viewing and control are available locally — it is your own
hardware.

---

## Concurrency

You choose how many browsers run at once: a total concurrency limit and a
per-engine limit.

> **Warning:** Higher concurrency uses more of your local CPU, memory, and
> network. Each running browser is a real engine process. Start low and raise it
> only as far as your machine comfortably handles.

---

## What self-host includes

The self-host image runs the browser engines and the local API/MCP/dashboard on
your own compute, using your own IP. The managed cloud's automatic exit routing
is a cloud-only feature — self-host requests egress from your machine's own
network.

---

## Updating

```bash
docker compose pull    # fetch the newest image tag
docker compose up -d   # recreate the container on the new image
```

## Removing

```bash
docker compose down    # stop and remove the container
```
