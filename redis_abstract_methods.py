from abc import ABC, abstractmethod 

class RedisMethodsAbstraction(ABC):

    @abstractmethod
    def set_hash(self, hash_name, key, value):
        pass

    @abstractmethod
    def get_hash(self, hash_name, key):
        pass

    @abstractmethod
    def get_hash_dist(self, hash_name):
        pass 

    @abstractmethod
    def hash_check(self, hash_name, key):
        pass

    @abstractmethod
    def delete_hash(self, hash_name, key):
        pass
