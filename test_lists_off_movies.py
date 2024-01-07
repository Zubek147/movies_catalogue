# test_test.py
import pytest
from unittest.mock import patch
from main import app, tmdb_client
from config import API_TOKEN

@pytest.mark.parametrize("list_type", ["popular", "top_rated", "upcoming", "now_playing"])
def test_homepage_with_different_lists(list_type):
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'results': []}
        with app.test_client() as client:
            response = client.get(f'/?list_type={list_type}')
            assert response.status_code == 200
            mock_get.assert_called_once_with(f"https://api.themoviedb.org/3/movie/{list_type}", headers={'Authorization': f"Bearer {API_TOKEN}"})
