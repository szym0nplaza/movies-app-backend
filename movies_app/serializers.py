from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Account, Movie, Actor, Director


class MovieSerializer(ModelSerializer):
    director = serializers.CharField(source="director.name", read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year_of_production',
                  'image', 'description', 'actors', 'director']


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
