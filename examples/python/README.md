# Python examples

```bash
pip install ghostcrawl
export GHOSTCRAWL_API_KEY="gck_live_..."
```

The Python SDK is async — every call is awaited from inside an `async`
function, run with `asyncio.run(...)`.

| File | What it shows |
|------|---------------|
| `scrape.py` | Scrape one page. |
| `crawl.py` | Start a crawl run and read its status. |
| `extract.py` | Extract structured JSON against a schema. |
| `async_scrape.py` | Scrape several pages concurrently. |

Run any example:

```bash
python scrape.py
```
