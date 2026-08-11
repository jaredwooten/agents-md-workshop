# Current CLI entrypoint. Wired to app.orders_v2 (the active order code) —
# not app.models / the legacy module.
import argparse

from app.orders_v2 import service


def cmd_add(args: argparse.Namespace) -> None:
    order = service.add_order(title=args.title)
    print(f"added: {order.title} (#{order.id})")


def cmd_list(args: argparse.Namespace) -> None:
    orders = service.list_orders()
    for o in orders:
        mark = "x" if o.done else " "
        print(f"[{mark}] #{o.id} {o.title}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="orders")
    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add")
    add_p.add_argument("title")
    add_p.set_defaults(func=cmd_add)

    list_p = sub.add_parser("list")
    list_p.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
