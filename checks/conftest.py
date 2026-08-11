import os

import pytest


@pytest.fixture(autouse=True)
def _require_test_db_path():
    """Fails loudly if ORDERS_DB_PATH isn't set, which happens if you run
    `pytest` directly instead of `make test` / `make check`."""
    if "ORDERS_DB_PATH" not in os.environ:
        pytest.fail(
            "ORDERS_DB_PATH is not set. Run tests via `make test` or `make check`, "
            "not bare `pytest` — see docs/CONTRIBUTING.md."
        )
