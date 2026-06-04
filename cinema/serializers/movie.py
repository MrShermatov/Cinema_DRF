from ..models.movie import Movie
from rest_framework import serializers
from .actor import ActorSerializer
from .genre import GenreSerializer
from .director import DirectorSerializer

class MovieReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
