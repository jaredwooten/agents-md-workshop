import json
import os
from pathlib import Path

from app.orders_v2.models import Order

DB_PATH = Path(os.environ.get("ORDERS_DB_PATH", str(Path.home() / ".orders-v2.json")))


def load() -> list[Order]:
    if not DB_PATH.exists():
        return []
    data = json.loads(DB_PATH.read_text())
    return [Order.from_dict(d) for d in data]


def save(orders: list[Order]) -> None:
    DB_PATH.write_text(json.dumps([o.to_dict() for o in orders], indent=2))
