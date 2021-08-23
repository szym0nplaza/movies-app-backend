from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    image = models.ImageField(
        upload_to="actors/", default="directors/default.jpg")

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    image = models.ImageField(upload_to="directors/",
                              default="directors/default.jpg")

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year_of_production = models.DateField(default="2010-01-01")
    image = models.ImageField(
        upload_to="movies/", default="movies/video-camera.png")
    description = models.TextField()
    actors = models.ManyToManyField(
        Actor, related_name="actors", blank=True, null=True)
    director = models.ForeignKey(
        Director, related_name="director", on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=True)


class Star(models.Model):
    amount = models.FloatField()
    movie = models.ManyToManyField(Movie, related_name="movie")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
