from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="Login"),
    path('admin/', views.admin_panel, name="Admin panel"),  # admin
    path('manage-user/<int:pk>/', views.manage_users, name="Manage users"),
    path('logout/', views.user_logout, name="Logout"),
    path('register/', views.user_register, name="Register"),
    path('movies/', views.get_movies, name="Get movies"),
    path('add-movie/', views.add_movies, name="Add movie"),  # admin
    path('manage-movie/<int:pk>/', views.manage_movies,
         name="Manage movies"),  # admin
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
]
