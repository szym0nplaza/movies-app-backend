from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="Login"),
    path('admin/', views.admin_panel, name="Admin panel"),  # admin
    path('manage-user/<int:pk>/', views.manage_users, name="Manage users"),
    path('logout/', views.user_logout, name="Logout"),
    path('register/', views.user_register, name="Register"),
    path('movies/', views.get_movies, name="Get movies"),
    path('get-users/', views.get_users, name="Get users"),
    path('user-details/<int:pk>/', views.user_details, name="User details"),
    path('add-movie/', views.add_movies, name="Add movie"),  # admin
    path('manage-movie/<int:pk>/', views.manage_movies,
         name="Manage movies"),  # admin
    path('movie-details/<int:pk>/', views.movie_details,
         name="Movie details"),  # admin
    path('actors/', views.get_actors, name="Get actors"),
    path('add-actor/', views.add_actors, name="Add actor"),  # admin
    path('manage-actor/<int:pk>/', views.manage_actors,
         name="Manage actors"),  # admin
    path('actor-details/<int:pk>/', views.actor_details, name="Actor details"),
    path('directors/', views.get_directors, name="Get directors"),
    path('add-director/', views.add_director, name="Add director"),  # admin
    path('manage-director/<int:pk>/',
         views.manage_directors, name="Manage directors"),  # admin
    path('director-details/<int:pk>/',
         views.director_details, name="Director details"),
    path('get-director-id/<str:name>/',
         views.get_director_id, name="Director id"),
    path('rate-movie/',
         views.rate_movie, name="Rate movie"),
    path('get-ratings/<str:title>/',
         views.get_ratings, name="Get ratings"),
    path('toggle-movies/', views.toggle_movies, name="Toglle movies")
]
