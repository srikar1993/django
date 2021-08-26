from django.contrib import admin
from testApp.models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'release_date', 'hero', 'heroin']

admin.site.register(Movie, MovieAdmin)