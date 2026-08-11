"""Regenerates app/_generated_schema.py from the Order dataclass in
app/orders_v2/models.py (the ACTIVE model — not the legacy app/models.py).

Run via `make schema` after changing app/orders_v2/models.py.
"""
import dataclasses
from pathlib import Path

from app.orders_v2.models import Order

TYPE_NAMES = {int: "int", str: "str", bool: "bool", float: "float"}

OUT_PATH = Path(__file__).resolve().parent.parent / "app" / "_generated_schema.py"


def main() -> None:
    lines = [
        "# GENERATED FILE - DO NOT EDIT BY HAND.",
        "# Run `python scripts/generate_schema.py` (or `make schema`) after changing",
        "# app/orders_v2/models.py.",
        "",
        "ORDER_SCHEMA = {",
    ]
    for f in dataclasses.fields(Order):
        type_name = TYPE_NAMES.get(f.type, str(f.type))
        lines.append(f'    "{f.name}": "{type_name}",')
    lines.append("}")
    lines.append("")
    OUT_PATH.write_text("\n".join(lines))
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
