from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    photo = models.URLField(max_length=300)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default="2010-01-01")
    photo = models.URLField(max_length=300)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    year_of_production = models.DateField(default="2010-01-01")
    image = models.URLField(max_length=300)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, blank=True, null=True)
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
