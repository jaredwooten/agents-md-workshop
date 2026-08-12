# orders-service

A small order-tracking CLI with a layered structure (`orders_v2` active code, a
deliberately-kept legacy module, a reporting module, and a notifications module
with an unrelated "priority" concept). Used as a **workshop sample repo** —
it's built to be just complex enough that an agent has to actually orient
itself, not just grep once and be done.

## Quick start

```
uv sync
uv run orders add "write AGENTS.md"
uv run orders list
```

## What is this repo for?

You'll complete a series of code changes twice — once with your agent operating
"cold" (no AGENTS.md), once after you've written repo context for it — from
identical starting states, in two separate fresh agent sessions. After each
round, ask the agent to report its metrics and log the numbers on the
whiteboard.
