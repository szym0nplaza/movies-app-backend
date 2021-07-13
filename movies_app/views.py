from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer


##### MOVIES #####
@api_view(["GET"])
def get_movies(request):
    movie_serializer = MovieSerializer(Movie.objects.all(), many=True)
    return Response(movie_serializer.data, status=200)


@api_view(["POST"])
def add_movies(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Passed.", status=200)
    return Response("Invalid data.", status=500)


@api_view(["PUT", "DELETE"])
def manage_movies(request):
    if request.method == "PUT":
        movie = Movie.objects.get(id=request.data['id'])
        movie.title = request.data['title']
        movie.year_of_production = request.data['year_of_production']
        movie.image = request.data['image']
        movie.description = request.data['description']
        movie.save()
        return Response("Changed.", status=200)

    if request.method == "DELETE":
        Movie.objects.filter(id=request.data['id']).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.")


##### ACTORS #####
@api_view(["GET"])
def get_actors(request):
    actor_serializer = ActorSerializer(Actor.objects.all(), many=True)
    return Response(actor_serializer.data, status=200)


@api_view(["POST"])
def add_actors(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Passed.", status=200)
    return Response("Invalid data.", status=500)


@api_view(["PUT", "DELETE"])
def manage_actors(request):
    if request.method == "PUT":
        actor = Actor.objects.get(id=request.data['id'])
        actor.name = request.data['name']
        actor.date_of_birth = request.data['date_of_birth']
        actor.photo = request.data['photo']
        actor.save()
        return Response("Changed", status=200)

    if request.method == "DELETE":
        Actor.objects.filter(id=request.data['id']).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.", status=500)


@api_view(["POST"])
def actor_details(request):
    actor = Actor.objects.get(id=request.data['id'])
    movies = [str(x) for x in Movie.objects.filter(actors=actor)]
    return Response({
        "actor_info": ActorSerializer(actor).data,
        "movies": movies
    }, status=200)


##### DIRECTORS #####
@api_view(["GET"])
def get_directors(request):
    director = DirectorSerializer(Director.objects.all(), many=True)
    return Response(director.data, status=200)


@api_view(["POST"])
def add_director(request):
    serializer = DirectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Passed.", status=200)
    return Response("Invalid data.", status=500)


@api_view(["PUT", "DELETE"])
def manage_directors(request):
    if request.method == "PUT":
        director = Director.objects.get(id=request.data['id'])
        director.name = request.data['name']
        director.date_of_birth = request.data['date_of_birth']
        director.photo = request.data['photo']
        director.save()
        return Response("Changed", status=200)

    if request.method == "DELETE":
        Director.objects.filter(id=request.data['id']).delete()
        return Response("Deleted.", status=200)

    return Response("Forbidden request method.", status=500)


@api_view(["POST"])
def director_details(request):
    director = Director.objects.get(id=request.data['id'])
    movies = [str(x) for x in Movie.objects.filter(director=director)]
    return Response({
        "director_info": DirectorSerializer(director).data,
        "movies": movies
    }, status=200)
