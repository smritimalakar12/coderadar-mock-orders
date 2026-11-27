def export_row(order, payment):
    return f"{order['id']},{payment['amount']}"
