# Delivery notifications for order status changes (email/SMS/push).
# NOTE: "priority" here means notification-channel priority (how fast we
# attempt delivery), which is unrelated to order priority. Don't confuse
# the two — this module has nothing to do with the Order model.

PRIORITY_LEVELS = {"low": 3, "normal": 2, "high": 1}


def send_notification(message: str, priority: str = "normal") -> str:
    level = PRIORITY_LEVELS.get(priority, PRIORITY_LEVELS["normal"])
    return f"[priority={level}] {message}"
