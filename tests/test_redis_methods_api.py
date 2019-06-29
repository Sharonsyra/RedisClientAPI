import unittest
import os

from containers import Configs, Readers
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
        self.hash_one = 'in'
        self.hash_two = 'ddf'
        self.hash_three = 'zf'
        self.hash_four = 'df'
        self.key = 'color'
        self.value = 'pink'
        self.test_redis_methods = Readers.redis_methods()

    def test_redis_set_existing_hash(self):
        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.hash_one, self.key, self.value))
        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.hash_name, self.key, self.value))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Exists', str(response.data))

    def test_redis_get_non_existing_hash(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}/{}'.format(self.hash_one, self.key)
        )
        self.assertIn('No hash', str(response.data))

    def test_redis_get_non_existing_dict_hash(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}'.format(self.hash_four)
        )
        self.assertIn('No dict', str(response.data))
    
    def test_redis_non_existing_hash_check(self):
        response = app.test_client().get(
            '/api/v1.0/methods/check/{}/{}'.format(self.hash_name, self.key)
        )
        self.assertIn('false', str(response.data))

    def test_redis_non_existing_delete_hash(self):
        response = app.test_client().delete(
            '/api/v1.0/methods/{}/{}'.format(self.hash_three, self.key)
        )
        self.assertIn('not exist', str(response.data))
