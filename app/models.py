# LEGACY MODULE.
# This is the original (v1) order model. It is kept only so that
# app/reporting/summary.py can compute historical totals from old data.
# Current work belongs in app/orders_v2/ — do not modify this file.

import itertools
from dataclasses import dataclass, field

_id_counter = itertools.count(1)


@dataclass
class Order:
    title: str
    id: int = field(default_factory=lambda: next(_id_counter))
    done: bool = False

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict) -> "Order":
        o = cls(title=data["title"], id=data["id"], done=data.get("done", False))
        return o
