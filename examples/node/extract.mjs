// Extract structured JSON from a page against a schema.
//
//   npm install @ghostcrawl/sdk
//   export GHOSTCRAWL_API_KEY=gck_live_...
//   node extract.mjs

import { createGhostcrawlClient } from '@ghostcrawl/sdk';

const client = createGhostcrawlClient({ token: process.env.GHOSTCRAWL_API_KEY });

const result = await client.extract({
  url: 'https://example.com',
  schema: {
    type: 'object',
    properties: {
      title: { type: 'string' },
      summary: { type: 'string' },
    },
  },
});
// The API returns { url, data, token_estimate }; `data` holds the structured fields.
console.log(result.data ?? result);
