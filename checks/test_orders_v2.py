from app.orders_v2 import service


def test_add_and_list_order(tmp_path, monkeypatch):
    monkeypatch.setattr("app.orders_v2.repository.DB_PATH", tmp_path / "orders.json")
    order = service.add_order(title="ship widgets")
    listed = service.list_orders()
    assert any(o.id == order.id and o.title == "ship widgets" for o in listed)
