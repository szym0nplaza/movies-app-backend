from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies, name="Get movies"),
    path('add-movie/', views.add_movies, name="Add movie"),
    path('manage-movie/<int:pk>/', views.manage_movies, name="Manage movies"),
    path('actors/', views.get_actors, name="Get actors"),
    path('add-actor/', views.add_actors, name="Add actor"),
    path('manage-actor/<int:pk>/', views.manage_actors, name="Manage actors"),
    path('actor-details/<int:pk>/', views.actor_details, name="Actor details"),
    path('directors/', views.get_directors, name="Get directors"),
    path('add-director/', views.add_director, name="Add director"),
    path('manage-director/<int:pk>/',
         views.manage_directors, name="Manage directors"),
    path('director-details/<int:pk>/',
         views.director_details, name="Director details"),
]
