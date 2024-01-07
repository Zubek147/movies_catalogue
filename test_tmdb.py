import unittest
from unittest.mock import patch, Mock
from tmdb_client import get_single_movie, get_movie_images, get_single_movie_cast

class TestTMDBClient(unittest.TestCase):

    @patch('tmdb_client.call_tmdb_api')
    def test_get_single_movie(self, mock_call_tmdb_api):
        movie_id = 123
        expected_response = {'id': movie_id, 'title': 'Test Movie'}
        mock_call_tmdb_api.return_value = expected_response

        result = get_single_movie(movie_id)

        mock_call_tmdb_api.assert_called_once_with(f"movie/{movie_id}")
        self.assertEqual(result, expected_response)

    @patch('tmdb_client.call_tmdb_api')
    def test_get_movie_images(self, mock_call_tmdb_api):
        movie_id = 123
        expected_response = {'backdrops': [], 'posters': []}
        mock_call_tmdb_api.return_value = expected_response

        result = get_movie_images(movie_id)

        mock_call_tmdb_api.assert_called_once_with(f"movie/{movie_id}/images")
        self.assertEqual(result, expected_response)

    @patch('tmdb_client.call_tmdb_api')
    def test_get_single_movie_cast(self, mock_call_tmdb_api):
        movie_id = 123
        expected_response = {"cast": []}
        mock_call_tmdb_api.return_value = expected_response

        result = get_single_movie_cast(movie_id)

        mock_call_tmdb_api.assert_called_once_with(f"movie/{movie_id}/credits")
        self.assertEqual(result, expected_response["cast"])

if __name__ == '__main__':
    unittest.main()
