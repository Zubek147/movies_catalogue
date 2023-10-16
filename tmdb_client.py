import requests
from config import API_TOKEN

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

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

