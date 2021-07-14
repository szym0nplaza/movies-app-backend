from django.contrib import admin
from .models import Movie, Account


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year_of_production',
                    'description', 'image')


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin')


admin.site.register(Account, AccountAdmin)
admin.site.register(Movie, MovieAdmin)
