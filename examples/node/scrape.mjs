// Scrape a single page with the GhostCrawl Node SDK.
//
//   npm install @ghostcrawl/sdk
//   export GHOSTCRAWL_API_KEY=gck_live_...
//   node scrape.mjs

import { createGhostcrawlClient } from '@ghostcrawl/sdk';

// Reads GHOSTCRAWL_API_KEY from the environment, or pass token: explicitly.
const client = createGhostcrawlClient({ token: process.env.GHOSTCRAWL_API_KEY });

const result = await client.scrape({ url: 'https://example.com', engine: 'chrome', format: 'markdown' });
console.log(result.content ?? result.markdown);
