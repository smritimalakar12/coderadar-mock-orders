def charge(order_id, amt):
    body = {'order_id': order_id, 'total_amount': amt}
    return body
