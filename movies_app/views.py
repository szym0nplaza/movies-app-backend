from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


@api_view(["GET"])
def get_movies(request):
    movie_serializer = MovieSerializer(Movie.objects.all(), many=True)
    return Response(movie_serializer.data)


@api_view(["POST"])
def add_movies(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("200")
    else:
        return Response("Invalid data.")


@api_view(["PUT", "DELETE"])
def manage_movies(request):
    if request.method == "PUT":
        movie = Movie.objects.get(id=request.data['id'])
        movie.title = request.data['title']
        movie.year_of_production = request.data['year_of_production']
        movie.image = request.data['image']
        movie.description = request.data['description']

        movie.save()
        return Response("200")

    if request.method == "DELETE":
        Movie.objects.filter(id=request.data['id']).delete()
        return Response("200")

    return Response("Forbidden request method.")
