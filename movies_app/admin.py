from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year_of_production', 'description',
                    'image')


admin.site.register(Movie, MovieAdmin)
