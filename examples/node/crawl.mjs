// Start a crawl run and read its status.
//
//   npm install @ghostcrawl/sdk
//   export GHOSTCRAWL_API_KEY=gck_live_...
//   node crawl.mjs

import { createGhostcrawlClient } from '@ghostcrawl/sdk';

const client = createGhostcrawlClient({ token: process.env.GHOSTCRAWL_API_KEY });

const run = await client.crawlRuns.start({
  url: 'https://example.com',
  maxDepth: 2,
  maxPages: 25,
});
const runId = run.run_id;
console.log('run id:', runId);

const status = await client.crawlRuns.get(runId);
console.log('status:', status);
