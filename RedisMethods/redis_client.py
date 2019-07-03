import redis

class RedisClient(object):
    
    def __init__(self, config):
        self._config = config
        self.connect(self._config)
        
    def connect(self, config):
        try:
            self._client = redis.Redis(config.get('host'), config.get('port'), config.get('db'))
        except Exception as e:
            raise e

    def set_hash(self, hash_name, key, value):
        return self._client.hset(hash_name, key, value)

    def get_hash(self, hash_name, key):
        return self._client.hget(hash_name, key)

    def get_hash_dict(self, hash_name):
        return self._client.hgetall(hash_name)

    def hash_check(self, hash_name, key):
        return self._client.hexists(hash_name, key)

    def delete_hash(self, hash_name, key):
        return self._client.hdel(hash_name, key)
