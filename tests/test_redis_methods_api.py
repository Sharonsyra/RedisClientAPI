import unittest
import os

from RedisMethods.containers import Configs, Readers
from main import app

class TestRedisMethodsAPI(unittest.TestCase):
    def setUp(self):
        Configs.config.override({
        "host": os.getenv('SERVER_HOST'),
        "port": os.getenv('PORT_NUMBER'),
        "db": os.getenv('DB_VALUE')
        })

        self.client = app.test_client
        self.hash_name = 'pk'
        self.another_hash_name = 'in'
        self.key = 'color'
        self.value = 'pink'
        self.test_redis_methods = Readers.redis_methods()
        self.test_redis_methods.delete_hash(self.hash_name, self.key)

    def test_redis_set_non_existing_hash(self):
        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.another_hash_name, self.key, self.value))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Created', str(response.data))

    def test_redis_set_existing_hash(self):
        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.hash_name, self.key, self.value))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Exists', str(response.data))

    def test_redis_get_existing_hash(self):
        response = app.test_client().get(
           '/api/v1.0/methods/{}/{}'.format(self.hash_name, self.key))
        self.assertIn('Hash', str(response.data))

    def test_redis_get_non_existing_hash(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}/{}'.format(self.another_hash_name, self.key)
        )
        self.assertIn('None', str(response.data))

    def test_redis_get_existing_dict_hash(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}'.format(self.hash_name)
        )
        self.assertIn('Hash Dict', str(response.data))

    def test_redis_get_non_existing_dict_hash(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}'.format(self.another_hash_name)
        )
        self.assertIn('None', str(response.data))

    def test_redis_existing_hash_check(self):
        response = app.test_client().get(
            '/api/v1.0/methods/check/{}/{}'.format(self.hash_name, self.key)
        )
        self.assertIn('true', str(response.data))
    
    def test_redis_non_existing_hash_check(self):
        response = app.test_client().get(
            '/api/v1.0/methods/check/{}/{}'.format(self.hash_name, self.key)
        )
        self.assertIn('false', str(response.data))

    def test_redis_existing_delete_hash(self):
        response = app.test_client().delete(
            '/api/v1.0/methods/{}/{}'.format(self.hash_name, self.key)
        )
        self.assertIn('Deleted', str(response.data))

    def test_redis_non_existing_delete_hash(self):
        response = app.test_client().delete(
            '/api/v1.0/methods/{}/{}'.format(self.another_hash_name, self.key)
        )
        self.assertIn('not exist', str(response.data))
