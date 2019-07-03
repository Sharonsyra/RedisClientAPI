from unittest.mock import Mock
import unittest
import os

from RedisMethods.redis_methods import RedisHashMethods
from containers import Configs, Readers, Clients

class TestRedisMethods(unittest.TestCase):

    def setUp(self):
        Configs.config.override({
        "host": os.getenv('SERVER_HOST'),
        "port": os.getenv('PORT_NUMBER'),
        "db": os.getenv('DB_VALUE')
        })
        self.test_redis_methods = Readers.redis_methods()
        self.hash_name = 'er'
        self.key = 'foo'
        self.value = 'bar'
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        self.mock_client = Mock()
        self.mock_client.set_hash.return_value = '1'
        self.mock_client.get_hash.return_value = "b'bar'"
        self.mock_client.get_hash_dict.return_value = "b'bar'"
        self.mock_client.hash_check.return_value = True
        self.mock_client.delete_hash.return_value = 1
        self.hash_methods = RedisHashMethods(self.mock_client)

    def test_set_hash_successful(self):
        self.hash_name = 'test_key'

        actual = self.hash_methods.set_hash(self.hash_name, self.key, self.value)

        self.assertEqual(actual, '1')
        self.mock_client.set_hash.assert_called_with(self.hash_name, self.key, self.value)

    def test_set_hash_failure_non_existing_hash(self):
        self.mock_client.set_hash.return_value = '0'

        actual = self.hash_methods.set_hash(self.hash_name, self.key, self.value)

        self.assertEqual(actual, '0')
        self.mock_client.set_hash.assert_called_with(self.hash_name, self.key, self.value)

    def test_get_hash_successful(self):
        actual = self.hash_methods.get_hash(self.hash_name, self.key)

        self.assertEqual(actual, "b'bar'")
        self.mock_client.get_hash.assert_called_with(self.hash_name, self.key)

    def test_get_hash_failure_non_existing_hash(self):
        self.mock_client.get_hash.return_value = "No matching value!"

        self.hash_name = 'test_key'

        actual = self.hash_methods.get_hash(self.hash_name, self.key)

        self.assertEqual(actual, "No matching value!")
        self.mock_client.get_hash.assert_called_with(self.hash_name, self.key)

    def test_get_dict_hash_successful(self):
        actual = self.hash_methods.get_hash_dict(self.hash_name)

        self.assertIn("b'bar'", actual)
        self.mock_client.get_hash_dict.assert_called_with(self.hash_name)

    def test_get_dict_hash_failure_non_existing_hash(self):
        self.mock_client.get_hash_dict.return_value = "No matching hash!"

        self.hash_name = 'test_key'

        actual = self.hash_methods.get_hash_dict(self.hash_name)

        self.assertIn("No matching hash!", actual)
        self.mock_client.get_hash_dict.assert_called_with(self.hash_name)

    def test_hash_check_successful(self):
        actual = self.hash_methods.hash_check(self.hash_name, self.key)

        self.assertTrue(actual)
        self.mock_client.hash_check.assert_called_with(self.hash_name, self.key)

    def test_hash_check_failure_non_existing_hash(self):
        self.hash_name = 'test_key'

        self.mock_client.hash_check.return_value = False

        actual = self.hash_methods.hash_check(self.hash_name, self.key)
        self.assertFalse(actual)
        self.mock_client.hash_check.assert_called_with(self.hash_name, self.key)

    def test_delete_hash_successful(self):
        actual = self.hash_methods.delete_hash(self.hash_name, self.key)

        self.assertEqual(actual, 1)
        self.mock_client.delete_hash.assert_called_once_with(self.hash_name, self.key)
    
    def test_delete_hash_failure_non_existing_hash(self):
        self.hash_name = 'test_key'

        self.mock_client.delete_hash.return_value = 0

        actual = self.hash_methods.delete_hash(self.hash_name, self.key)

        self.assertEqual(actual, 0)
        self.mock_client.delete_hash.assert_called_once_with(self.hash_name, self.key)

if __name__ == '__main__':
    unittest.main(exit=False)
