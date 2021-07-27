from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from .models import Movie, Actor, Director, Account
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer, AccountSerializer, UserSerializer
from django.contrib.auth import login, logout
from .backends import AuthBackend
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser


##### LOGIN AND REGISTRATION #####
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    email, password = request.data.values()
    user = AuthBackend.authenticate(email=email, password=password)
    if user is not None:
        is_admin = AccountSerializer(Account.objects.get(user=user))
        user_id = UserSerializer(User.objects.get(username=email))
        login(request, user)
        token = str(Token.objects.get_or_create(user=user)[0])
        return Response({
            "id": user_id.data['id'],
            "email": email,
            "is_admin": is_admin.data['is_admin'],
            "token": token
        }, status=200)
    return Response("Invalid data.", status=400)


@api_view(["POST"])
@permission_classes([AllowAny])
def user_logout(request):
    email = request.data['email']
    user = User.objects.get(email=email)
    user.auth_token.delete()
    logout(request)
    return Response("Logget out.", status=200)


@api_view(["POST"])
def user_register(request):
    email, password, password2 = request.data.values()
    if password != password2:
        return Response("Passwords does not match.", status=400)
    try:
        user = User.objects.create_user(
            username=email, email=email, password=password)
        Account.objects.create(user=user)
        return Response("Registered.", status=200)
    except:
        return Response("Invalid data.", status=400)


@api_view(["GET"])
def admin_panel(request):
    user = AuthBackend.authenticate(email=request.data['email'])
    permissions = AccountSerializer(Account.objects.get(user=user))
    if permissions.data['is_admin']:
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(serializer.data, status=200)
    return Response("Access denied. You don't have permissions", status=403)


@api_view(["DELETE", "PUT"])
def manage_users(request, pk):
    try:
        if request.method == "PUT":
            user = User.objects.get(id=pk)
            user.email = request.data['email']
            user.set_password(request.data['password'])
            user.save()
            return Response("Changed.", status=200)

        if request.method == "DELETE":
            user = User.objects.get(id=pk)
            user.delete()
            return Response(f"Deleted user with email {user}", status=200)
    except:
        return Response("Invalid data.", status=400)


@api_view(["GET"])
def get_users(request):
    users = UserSerializer(User.objects.all(), many=True)
    return Response(users.data, status=200)


@api_view(["GET"])
def user_details(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    is_admin = AccountSerializer(Account.objects.get(user=user))
    try:
        Token.objects.get(user=user)
        is_logged = True
    except:
        is_logged = False
    print(user, is_admin.data['is_admin'], is_logged)
    return Response({
        "email": serializer.data['email'],
        "is_admin": is_admin.data['is_admin'],
        "is_logged": is_logged
    }, status=200)

##### MOVIES #####


@ api_view(["GET"])
def get_movies(request):
    movie_serializer = MovieSerializer(Movie.objects.all(), many=True)
    return Response(movie_serializer.data, status=200)


@ api_view(["POST"])
@ parser_classes([MultiPartParser, FormParser])
def add_movies(request):
    if len(Movie.objects.filter(title=request.data['title'])) != 0:
        return Response("Movie exists.", status=400)
    rd = request.data
    director = Director.objects.get(name=rd['director'])
    data = {"title": rd['title'], "year_of_production": rd['year_of_production'],
            "image": rd['image'], "description": rd['description']}
    serializer = MovieSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        movie = Movie.objects.get(title=rd['title'])
        movie.director = director
        for actor in rd['actors'].split(','):
            actor_object = Actor.objects.get(name=actor)
            movie.actors.add(actor_object)
        movie.save()
        return Response("Passed.", status=200)
    return Response("Invalid data.", status=500)


@ api_view(["PUT", "DELETE"])
def manage_movies(request, pk):
    if request.method == "PUT":
        movie = Movie.objects.get(id=pk)
        movie.title = request.data['title']
        movie.year_of_production = request.data['year_of_production']
        movie.image = request.data['image']
        movie.description = request.data['description']
        movie.save()
        return Response("Changed.", status=200)

    if request.method == "DELETE":
        Movie.objects.get(id=pk).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.")


@ api_view(["GET"])
def movie_details(request, pk):
    return Response(MovieSerializer(Movie.objects.get(id=pk)).data, status=200)

##### ACTORS #####


@ api_view(["GET"])
def get_actors(request):
    actor_serializer = ActorSerializer(Actor.objects.all(), many=True)
    return Response(actor_serializer.data, status=200)


@ api_view(["POST"])
@ parser_classes([MultiPartParser, FormParser])
def add_actors(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Passed.", status=200)
    return Response("Invalid data.", status=500)


@ api_view(["PUT", "DELETE"])
def manage_actors(request, pk):
    if request.method == "PUT":
        actor = Actor.objects.get(id=pk)
        actor.name = request.data['name']
        actor.date_of_birth = request.data['date_of_birth']
        actor.photo = request.data['photo']
        actor.save()
        return Response("Changed", status=200)

    if request.method == "DELETE":
        Actor.objects.get(id=pk).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.", status=500)


@ api_view(["GET"])
def actor_details(request, pk):
    actor = Actor.objects.get(id=pk)
    movies = [str(x) for x in Movie.objects.filter(actors=actor)]
    return Response({
        "actor_info": ActorSerializer(actor).data,
        "movies": movies
    }, status=200)


##### DIRECTORS #####
@ api_view(["GET"])
def get_directors(request):
    director = DirectorSerializer(Director.objects.all(), many=True)
    return Response(director.data, status=200)


@ api_view(["POST"])
@ parser_classes([MultiPartParser, FormParser])
def add_director(request):
    serializer = DirectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Passed.", status=200)

    return Response("Invalid data.", status=500)


@ api_view(["PUT", "DELETE"])
def manage_directors(request, pk):
    if request.method == "PUT":
        director = Director.objects.get(id=pk)
        director.name = request.data['name']
        director.date_of_birth = request.data['date_of_birth']
        director.photo = request.data['photo']
        director.save()
        return Response("Changed", status=200)

    if request.method == "DELETE":
        Director.objects.get(id=pk).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.", status=500)


@ api_view(["GET"])
def director_details(request, pk):
    director = Director.objects.get(id=pk)
    movies = [str(x) for x in Movie.objects.filter(director=director)]
    return Response({
        "director_info": DirectorSerializer(director).data,
        "movies": movies
    }, status=200)
