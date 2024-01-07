import requests
from config import API_TOKEN

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type="popular"):
    return call_tmdb_api(f"movie/{list_type}")


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Błąd podczas pobierania danych:", response.status_code)
        return None
    
def get_poster_url(poster_path, size = "w342"):
    base_url = "https://image.tmdb.org/t/p"
    return f"{base_url}/{size}/{poster_path}"

def get_bcakdrop_url(backdrop_path, size = "w780"):
    base_url = "https://image.tmdb.org/t/p"
    return f"{base_url}/{size}/{backdrop_path}"

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")


def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_available_lists():
    available_lists = {
        'popular': 'Popular',
        'top_rated': 'Top Rated',
        'upcoming': 'Upcoming',
        'now_playing': 'Now Playing'
    }
    return available_lists