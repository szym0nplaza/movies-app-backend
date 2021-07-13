from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    photo = models.URLField(max_length=300)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    year_of_production = models.DateField(default="2010-01-01")
    image = models.URLField(max_length=300)
    description = models.TextField()
    actors = models.ForeignKey(Actor, on_delete=models.CASCADE, blank=True)


class Director(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    photo = models.URLField(max_length=300)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
