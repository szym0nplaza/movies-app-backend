from django.urls import path
from .views import get_movies, add_movies, manage_movies

urlpatterns = [
    path('movies/', get_movies, name="Get movies"),
    path('add-movie/', add_movies, name="Add movie"),
    path('manage-movie/', manage_movies, name="Manage movies"),
]
