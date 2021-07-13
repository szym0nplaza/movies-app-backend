from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies, name="Get movies"),
    path('add-movie/', views.add_movies, name="Add movie"),
    path('manage-movie/', views.manage_movies, name="Manage movies"),
    path('actors/', views.get_actors, name="Get actors"),
    path('add-actor/', views.add_actors, name="Add actor"),
    path('manage-actor/', views.manage_actors, name="Manage actors"),
    path('actor-details/', views.actor_details, name="Actor details"),
    path('directors/', views.get_directors, name="Actor details"),
    path('add-director/', views.add_director, name="Actor details"),
    path('manage-director/', views.manage_directors, name="Actor details"),
    path('director-details/', views.director_details, name="Actor details"),
]
