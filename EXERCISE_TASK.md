# Exercise task (give this to your agent verbatim — both rounds, word for word)

> Add a `priority` field to Order: an integer, 1 (highest) to 5 (lowest), defaulting to 3.
> Expose it as an optional `--priority` flag on `orders add`.
> Show priority in the output of `orders list`, sorted with highest priority first.
> Keep all checks green and lint clean before you're done.

Deliberately vague on purpose: "Order" and "priority" both exist in more than one place in this repo. Don't clarify further if your agent asks — let it work it out (or not) from the repo itself.

## Definition of done

- [ ] `make check` passes (tests + lint)
- [ ] `orders add "x" --priority 1` and `orders list` both work from a clean clone
- [ ] The change landed in `app/orders_v2/`, not the legacy module
- [ ] No hand-edits to `app/_generated_schema.py`
- [ ] `app/notifications/` untouched
- [ ] Commit message follows the repo's convention

## Before you start each round

1. `git status` must be clean (no leftover edits from a previous round) — reset if not.
2. Start a **brand-new agent session/conversation** — not a continuation of a previous round's chat. A continuing session already has files in context, which will make the round look artificially cheap and invalidate the comparison.
