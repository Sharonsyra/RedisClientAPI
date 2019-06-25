from flask import Flask

from containers import Configs, Readers, Clients

app = Flask(__name__)

Configs.config.override({
        "host": "localhost",
        "port": "6379",
        "db": 0
})

redis_methods = Readers.redis_methods()

print(redis_methods.set_hash('er', 'foo', 'bar'))
print(redis_methods.get_hash('er', 'foo'))
print(redis_methods.get_hash_dist('er'))
print(redis_methods.hash_check('er', 'foo'))
print(redis_methods.delete_hash('er', 'foo'))

if __name__ == "__main__":
    app.run(debug=True)
