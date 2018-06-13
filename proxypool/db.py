import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import HOST, PORT,POOL_NAME
redis_pool = redis.ConnectionPool(host=HOST, port=PORT, max_connections=20)

class RedisClient(object):
    def __init__(self):
        self._conn = redis.Redis(connection_pool=redis_pool)

    def get(self, total=1):
        """
        get proxies from redis
        """
        tmp = self._conn.smembers(POOL_NAME)
        # tmp = self._conn.srandmember(POOL_NAME, total)
        return [s.decode('utf-8') for s in tmp]

    def put(self, proxy):
        """
        add proxy to right top
        """
        self._conn.sadd(POOL_NAME, proxy)

    def pop(self):
        """
        get proxy from right.
        """
        return self._conn.spop(POOL_NAME).decode('utf-8')

    @property
    def queue_len(self):
        """
        get length from queue.
        """
        return self._conn.scard(POOL_NAME)

    def flush(self):
        """
        flush db
        """
        self._db.flushall()


