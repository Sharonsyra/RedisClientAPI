from .redis_abstract_methods import RedisMethodsAbstraction

class RedisHashMethods(RedisMethodsAbstraction):
    
    def __init__(self, client):
        try:
            self._client = client
        except Exception as e:
            raise e
            
    def set_hash(self, hash_name, key, value):
        return self._client.set_hash('er', 'foo', 'bar')

    def get_hash(self, hash_name, key):
        output = self._client.get_hash(hash_name, key)
        if output is None:
            return "No matching value!"
        return output

    def get_hash_dist(self, hash_name):
        output = self._client.get_hash_dist(hash_name)
        if not output:
            return "No matching hash!"
        return output

    def hash_check(self, hash_name, key):
        return self._client.hash_check(hash_name, key)

    def delete_hash(self, hash_name, key):
        output = self._client.delete_hash(hash_name, key)
        if output is None:
            return 0
        return output
