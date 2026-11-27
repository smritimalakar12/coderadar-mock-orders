def retry_failed(conn, order_id, attempts=5):
    for _ in range(attempts):
        sql = "UPDATE payments SET status='retry' WHERE order_id='" + order_id + "'"
        conn.execute(sql)  # no backoff, string-built SQL
