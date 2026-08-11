# Sanity test for the LEGACY module only (app/models.py). Do not extend this
# file for new order features — that's checks/test_orders_v2.py.
from app.models import Order


def test_legacy_order_roundtrip():
    o = Order(title="legacy order")
    d = o.to_dict()
    o2 = Order.from_dict(d)
    assert o2.title == o.title
    assert o2.id == o.id
    assert o2.done is False
