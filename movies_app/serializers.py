from rest_framework.serializers import ModelSerializer
from .models import Movie, Actor, Director


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"
