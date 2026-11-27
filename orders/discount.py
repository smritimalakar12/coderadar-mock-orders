def apply_discount(order, pct):
    return order['total'] * (1 - pct/100)
