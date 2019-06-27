# from mock import Mock
from mock import patch
from unittest.mock import MagicMock
import unittest
import os

from RedisMethods.redis_methods import RedisHashMethods
from RedisMethods.containers import Configs, Readers, Clients

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
        self.another_hash_name = 'two'
        self.value = 'bar'

    @patch('RedisMethods.containers.Readers')
    def test_set_non_existing_hash(self, mock_set_hash):
        self.test_redis_methods.delete_hash(self.hash_name, self.key)
        mock_set_hash.return_value = "{}".format(self.test_redis_methods.set_hash(self.hash_name, self.key, self.value))
        self.assertEqual(mock_set_hash.return_value, '1')

    @patch('RedisMethods.containers.Readers')
    def test_set_existing_hash(self, mock_set_hash):
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        mock_set_hash.return_value = "{}".format(self.test_redis_methods.set_hash(self.hash_name, self.key, self.value))
        self.assertEqual(mock_set_hash.return_value, '0')

    @patch('RedisMethods.containers.Readers')    
    def test_get_existing_hash(self, mock_get_hash): 
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        mock_get_hash.return_value = "{}".format(self.test_redis_methods.get_hash(self.hash_name, self.key))        
        self.assertEqual(mock_get_hash.return_value, "b'bar'")

    @patch('RedisMethods.containers.Readers')    
    def test_get_non_existing_hash(self, mock_get_hash): 
        mock_get_hash.return_value = "{}".format(self.test_redis_methods.get_hash(self.another_hash_name, self.key))        
        self.assertEqual(mock_get_hash.return_value, "No matching value!")

    @patch('RedisMethods.containers.Readers')    
    def test_get_existing_dict_hash(self, mock_get_dict_hash): 
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        mock_get_dict_hash.return_value = "{}".format(self.test_redis_methods.get_hash_dist(self.hash_name))        
        self.assertIn("b'bar'", str(mock_get_dict_hash.return_value))       

    @patch('RedisMethods.containers.Readers')    
    def test_get_non_existing_dict_hash(self, mock_get_dict_hash): 
        mock_get_dict_hash.return_value = "{}".format(self.test_redis_methods.get_hash_dist(self.another_hash_name)) 
        self.assertEqual(mock_get_dict_hash.return_value, "No matching hash!")

    @patch('RedisMethods.containers.Readers')    
    def test_existing_hash_check(self, mock_hash_check): 
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        mock_hash_check.return_value = self.test_redis_methods.hash_check(self.hash_name, self.key)
        self.assertTrue(mock_hash_check.return_value)

    @patch('RedisMethods.containers.Readers')    
    def test_non_existing_hash_check(self, mock_hash_check): 
        mock_hash_check.return_value = self.test_redis_methods.hash_check(self.another_hash_name, self.key)
        self.assertFalse(mock_hash_check.return_value) 

    @patch('RedisMethods.containers.Readers')
    def test_existing_delete_hash(self, mock_detele_hash):
        self.test_redis_methods.set_hash(self.hash_name, self.key, self.value)
        mock_detele_hash.return_value = self.test_redis_methods.delete_hash(self.hash_name, self.key)
        self.assertEqual(mock_detele_hash.return_value, 1)
    
    @patch('RedisMethods.containers.Readers')
    def test_non_existing_delete_hash(self, mock_detele_hash):
        mock_detele_hash.return_value = self.test_redis_methods.delete_hash(self.hash_name, self.key)
        self.assertEqual(mock_detele_hash.return_value, 1)
    

if __name__ == '__main__':
    unittest.main(exit=False)