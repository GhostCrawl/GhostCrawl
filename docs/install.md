# Install

ghostcrawl ships two ways to install: the SDKs (for talking to the managed
cloud) and the self-host Docker image (for running locally).

---

## SDKs (cloud)

**Python:**

```bash
pip install ghostcrawl
```

Requires Python 3.10+.

**Node:**

```bash
npm install @ghostcrawl/sdk
```

Requires Node.js 18+.

The Node CLI (`@ghostcrawl/cli`) and Python CLI (`ghostcrawl`) also ship `init`
and `install` helpers for saving your API key and a local install directory.

---

## Self-host (Docker)

The self-host image runs via Docker Compose.

### First run

```bash
cp docker-compose.yml.template docker-compose.yml
echo "GHOSTCRAWL_API_KEY=gck_live_..." > .env   # in the same directory
docker compose up -d                            # launch locally
docker compose logs -f                          # follow the logs
```

This launches the container with a local API (`http://localhost:8000`), MCP
(`http://localhost:3143`), and dashboard.

### Requirements

- A container runtime (Docker or Podman with the `compose` plugin).
- A valid API key. Sign up to obtain one — the key gates the image, and the
  self-host runtime validates it online every time it starts.
- Outbound network access to the ghostcrawl API for the start-time license
  check (there is no offline mode).

### Getting a key

Create an account, verify your email, log in, and mint an API key from your
dashboard. That key goes in the `.env` file beside your `docker-compose.yml`.

---

## Verifying

```bash
docker compose ps          # container state
curl http://localhost:8000/healthz   # local API health
```

A healthy instance reports the container as running and the local API as
reachable.
