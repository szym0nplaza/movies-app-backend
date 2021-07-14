from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Account, Movie, Actor, Director


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


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
