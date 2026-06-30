# CLI examples

```bash
npm install -g @ghostcrawl/cli
export GHOSTCRAWL_API_KEY="gck_live_..."
```

See [`commands.sh`](commands.sh) for a runnable tour. Common commands:

```bash
# Scrape a page (Markdown output)
ghostcrawl scrape https://example.com --format markdown

# Start a crawl run
ghostcrawl crawl https://example.com --max-depth 2 --max-pages 25

# Extract structured data — --schema takes the path to a JSON Schema file
ghostcrawl extract https://example.com --schema ./schema.json

# Discover all reachable URLs from a seed
ghostcrawl map https://example.com

# Check who you are and your current usage
ghostcrawl auth whoami
ghostcrawl usage
```

Run `ghostcrawl --help` for the full command list. The same `ghostcrawl`
command also helps set up local runs via `init` (save your API key) and
`install` — see the [self-host guide](../../docs/usage-selfhost.md).
