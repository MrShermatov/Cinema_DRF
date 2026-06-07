from django.db import models
from .actor import Actor
from .director import Director
from .genre import Genre
class Movie(models.Model):
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=500)
    release_year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title