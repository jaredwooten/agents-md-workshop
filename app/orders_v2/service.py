from app.orders_v2 import repository
from app.orders_v2.models import Order


def add_order(title: str) -> Order:
    orders = repository.load()
    order = Order(title=title)
    orders.append(order)
    repository.save(orders)
    return order


def list_orders() -> list[Order]:
    return repository.load()
