#!/usr/bin/env bash
# Start a crawl run from a seed URL, then poll it to completion.
# Usage: GHOSTCRAWL_API_KEY=gck_live_... ./crawl.sh [SEED_URL]
set -euo pipefail

SEED="${1:-https://example.com}"
AUTH="Authorization: Bearer ${GHOSTCRAWL_API_KEY:?set GHOSTCRAWL_API_KEY}"

# Kick off a crawl run. The /v1/crawl-runs body is a tagged union keyed on
# `action`; the start verb takes `action: "start"` and a `seed_urls` list.
RUN=$(curl -sS https://api.ghostcrawl.io/v1/crawl-runs \
  -H "$AUTH" -H "Content-Type: application/json" \
  -d "{\"action\": \"start\", \"seed_urls\": [\"${SEED}\"], \"max_depth\": 2, \"max_pages\": 25}")

echo "Created run:"
echo "$RUN"

RUN_ID=$(echo "$RUN" | sed -n 's/.*"run_id"[ :]*"\([^"]*\)".*/\1/p')
echo "Run id: ${RUN_ID}"

# Poll status.
curl -sS "https://api.ghostcrawl.io/v1/crawl-runs/${RUN_ID}" -H "$AUTH"
