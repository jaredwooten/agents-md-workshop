.PHONY: check test lint schema

ORDERS_DB_PATH ?= /tmp/orders-service-test.json

test:
	ORDERS_DB_PATH=$(ORDERS_DB_PATH) uv run pytest checks/

lint:
	uv run ruff check --config tooling/ruff.toml .

check: test lint

schema:
	uv run python scripts/generate_schema.py
