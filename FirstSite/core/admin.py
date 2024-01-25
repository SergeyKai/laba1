from django.contrib import admin
from .models import Film, Actor, FilmImages

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(FilmImages)
