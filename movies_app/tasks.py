from celery import shared_task
import requests
from .models import Movie, Director
from decouple import config


@shared_task
def get_movies_data():
    key = config('API_KEY')
    try:
        for movie in range(99, 110):
            request = requests.get(
                f'https://api.themoviedb.org/3/movie/{movie}?api_key={key}').json()
            title = request['title']
            year_of_production = request['release_date']
            description = request['overview']
            Movie.objects.create(
                title=title, year_of_production=year_of_production, description=description)
    except:
        return True
