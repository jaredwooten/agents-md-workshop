# ACTIVE order model. This is the one you want if you're adding an order field.
# See app/_generated_schema.py, which is generated from this file — never hand-edit it.

from dataclasses import dataclass, field
import itertools

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
        return cls(title=data["title"], id=data["id"], done=data.get("done", False))
