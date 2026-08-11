# Contributing (read this before your PR, not before your first commit apparently)

- **Package manager**: `uv` only. Never `pip install` directly — it won't update `uv.lock` and CI will fail.
- **Tests live in `checks/`, not `tests/`.** Run them with `make check`, not `pytest` directly — `make check` also sets `ORDERS_DB_PATH` to a temp file, which the test fixtures require and which bare `pytest` will not set.
- **Lint config is at `tooling/ruff.toml`**, not repo root. Plain `ruff check .` picks up defaults instead. Use `make check` or `ruff check --config tooling/ruff.toml .`.
- **`app/_generated_schema.py` is generated.** Never hand-edit it. Run `python scripts/generate_schema.py` (or `make schema`) after changing `app/orders_v2/models.py` and commit the regenerated file.
- **Commit messages**: `type(scope): summary` — e.g. `feat(orders): add priority field`. No exceptions, a hook will reject anything else in the real org repo (not enforced in this sample, but pretend).
- **Env vars**: copy `.env.example` to `.env`, never commit real values.

## Module map (easy to get wrong)

- **`app/orders_v2/`** is the active order code. Anything new about orders — fields, behavior, CLI flags — belongs here.
- **`app/models.py`** and `app/cli.py`'s old counterpart are the **legacy (v1) order code**. It's only still around because `app/reporting/summary.py` needs it to reproduce historical totals from before the v2 migration. Do not add features here; do not "clean it up" as a drive-by.
- **`app/notifications/`** has its own, unrelated `priority` concept (delivery-channel priority — how fast we retry sending a message). It has nothing to do with order priority. If a task mentions "priority" and you land in this file, you're in the wrong place.
- **`app/reporting/`** intentionally imports the legacy module, not `orders_v2`. That's correct, not a bug.
