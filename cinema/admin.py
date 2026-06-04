from django.contrib import admin
from .models import Director, Genre, Movie, Actor

admin.site.register([Director, Genre, Movie, Actor])
