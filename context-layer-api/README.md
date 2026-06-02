# Context Layer API

Integration layer that syncs context from Slack, Stripe, Gong, PostHog, HubSpot, Attio, and customer help desks. Built with TypeScript, Express, and BullMQ for async job processing.

## Local Development
```bash
npm install
npm run dev
```

Requires Redis and PostgreSQL. Set up OAuth credentials for each integration in `.env`.