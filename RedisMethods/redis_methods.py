from .redis_abstract_methods import RedisMethodsAbstraction

class RedisHashMethods(RedisMethodsAbstraction):
    
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e
            
    def set_hash(self, hash_name, key, value):
        """Set a hash value to a key value pair equivalent to Redis hset()"""
        return self._client.set_hash(hash_name, key, value)

    def get_hash(self, hash_name, key):
        """Gets the value of the key within the hash name
        equivalent to Redis' hget()"""
        output = self._client.get_hash(hash_name, key)

        if output is None:
            return "No matching value!"
        return output

    def get_hash_dict(self, hash_name):
        """Gets a Python dict of the hash’s name/value pairs
        equivalent to Redis' hgetall()"""
        output = self._client.get_hash_dict(hash_name)

        if not output:
            return "No matching hash!"
        return output

    def hash_check(self, hash_name, key):
        """Returns a boolean value indicating if key exists within the hash name
        equivalent to Redis's hexists()"""
        return self._client.hash_check(hash_name, key)

    def delete_hash(self, hash_name, key):
        """Deletes keys from the hash name equivalent of Redis' hdel()"""
        output = self._client.delete_hash(hash_name, key)

        if output is None:
            return 0
        return output
