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
        self.hash_one = 'in'
        self.key = 'foo'
        self.value = 'bar'
        self.test_redis_methods = Readers.redis_methods()
        self.test_redis_methods.set_hash(self.hash_one, self.key, self.value)

    def test_redis_set_hash_successful(self):
        self.hash_one = 'test_key'

        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.hash_one, self.key, self.value)
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn('Created', str(response.data))

    def test_redis_set_hash_failure_for_existing_hash(self):
        response = app.test_client().post(
            '/api/v1.0/methods/{}/{}/{}'.format(self.hash_one, self.key, self.value)
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('Exists', str(response.data))

    def test_redis_get_hash_successful(self):
        response = app.test_client().get(
           '/api/v1.0/methods/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('Hash', str(response.data))

    def test_redis_get_hash_failure_non_existing_hash(self):
        self.hash_one = 'test_key'

        response = app.test_client().get(
            '/api/v1.0/methods/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('No hash', str(response.data))

    def test_redis_get_dict_hash_successful(self):
        response = app.test_client().get(
            '/api/v1.0/methods/{}'.format(self.hash_one)
        )

        self.assertIn('Hash Dict', str(response.data))

    def test_redis_get_dict_hash_failure_non_existing_hash(self):
        self.hash_one = 'test_key'

        response = app.test_client().get(
            '/api/v1.0/methods/{}'.format(self.hash_one)
        )

        self.assertIn('No dict', str(response.data))
    
    def test_redis_hash_check_successful(self):
        response = app.test_client().get(
            '/api/v1.0/methods/check/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('true', str(response.data))

    def test_redis_hash_check_failure_non_existing_hash(self):
        self.hash_one = 'test_key'

        response = app.test_client().get(
            '/api/v1.0/methods/check/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('false', str(response.data))

    def test_redis_delete_hash_successful(self):
        response = app.test_client().delete(
            '/api/v1.0/methods/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('Deleted', str(response.data))

    def test_redis_delete_hash_failure_non_existing_hash(self):
        self.hash_one = 'test_key'

        response = app.test_client().delete(
            '/api/v1.0/methods/{}/{}'.format(self.hash_one, self.key)
        )

        self.assertIn('not exist', str(response.data))

    def tearDown(self):
        self.test_redis_methods.delete_hash(self.hash_one, self.key)
