from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_of_production',
                    'image', 'description')


admin.site.register(Movie, MovieAdmin)
