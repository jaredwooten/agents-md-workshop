# Historical reporting. Intentionally imports the LEGACY order module
# (app/models.py, not app/orders_v2/) because old reports must match
# numbers generated before the v2 migration. This is expected and correct
# -- do not "fix" this import as part of an orders_v2 change.

from app.models import Order


def count_done(orders: list[Order]) -> int:
    return sum(1 for o in orders if o.done)
