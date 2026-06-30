#!/usr/bin/env bash
# A short tour of the GhostCrawl CLI.
#
#   npm install -g @ghostcrawl/cli
#   export GHOSTCRAWL_API_KEY=gck_live_...
#   ./commands.sh
set -euo pipefail

: "${GHOSTCRAWL_API_KEY:?set GHOSTCRAWL_API_KEY}"

# Who am I? (tier, email, team)
ghostcrawl auth whoami

# Scrape a single page (Markdown output).
ghostcrawl scrape https://example.com --format markdown

# Start a crawl run.
ghostcrawl crawl https://example.com --max-depth 2 --max-pages 25

# Extract structured data. --schema takes the path to a JSON Schema file.
cat > /tmp/ghostcrawl-schema.json <<'JSON'
{"type":"object","properties":{"title":{"type":"string"}}}
JSON
ghostcrawl extract https://example.com --schema /tmp/ghostcrawl-schema.json

# Discover all URLs reachable from a seed (no content scrape).
ghostcrawl map https://example.com

# Check your current usage.
ghostcrawl usage
