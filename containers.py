from dependency_injector import providers, containers

from redis_client import RedisClient
from redis_methods import RedisHashMethods

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')

class Clients(containers.DeclarativeContainer):
    redis_client = providers.Singleton(RedisClient, Configs.config)

class Readers(containers.DeclarativeContainer):
    redis_methods = providers.Factory(RedisHashMethods, client=Clients.redis_client)
