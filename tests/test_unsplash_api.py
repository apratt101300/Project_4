import unittest 
import requests
from unittest import TestCase
from unittest.mock import patch
from apis import unsplash_api


key =  'MMZ9lcnReyfxYUFX507ZrlD7lokdDdDyFYplI3Ze9FE'
url = 'https://api.unsplash.com/search/photos'

class TestUnsplashApi(TestCase):
    @patch('unsplash_api._unsplash_api_call')
    def test_api_query(self, mock_query):
        mock_query = {'query':'yosemite', 'per_page':4, 'client_id':key}
        example_response = requests.get(url, params=mock_query).json()

        example_query = {'query':'yosemite', 'per_page':4, 'client_id':key}
        expected_response = requests.get(url, params=example_query).json()
        
        self.assertEqual(expected_response, example_response)

if __name__ == '__main__':
    unittest.main()