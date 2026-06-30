# LangChain examples

```bash
pip install ghostcrawl-langchain
export GHOSTCRAWL_API_KEY="gck_live_..."
```

`ghostcrawl-langchain` exposes GhostCrawl's scrape / search / extract / crawl
surfaces as LangChain `BaseTool` subclasses, so an LLM agent can call them
directly.

| File | What it shows |
|------|---------------|
| `tool.py` | Invoke a GhostCrawl tool directly. |
| `agent.py` | Give the tools to a LangChain agent. |

Run:

```bash
python tool.py
```
