# Connection Pool Usage Notes

## When to Enable or Disable Connection Pool

- **Disable connection pool** if your proxy serves a small number of concurrent users (e.g., less than 200).  
  Creating a new TCP connection for each client is efficient enough and keeps the code simple.
- **Enable connection pool** if you expect a large number of concurrent users (hundreds or thousands).  
  The pool helps reduce connection latency and system resource usage by reusing existing connections to Telegram servers.

## Default Behavior in mtprotoproxy

- By default, the connection pool is disabled for low user counts (see `get_connection` in `TgConnectionPool`).
- To enable the pool, uncomment and adjust the relevant code in `get_connection` and use `register_host_port` to pre-create connections.

## Recommendation

- **< 200 concurrent users:** Pool is not necessary.
- **> 200–300 concurrent users:** Consider enabling the pool for better performance.
