from django.db.models import Model

from ..models.movie import Movie
from ..models.genre import Genre
from rest_framework import serializers

class GenreSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    # genres = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # genres = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    # genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # url = serializers.HyperlinkedIdentityField(view_name='genre-detail')
    class Meta:
        model = Genre

        fields = '__all__'

    def get_genre(self, obj):
        from serializers.genre import GenreSerializer
        return GenreSerializer(obj.genre, context=self.context).data

class GenreWriteSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(),
                                                  many=True,
                                                  write_only=True,
                                                  required=False)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'movie_id']

    def create(self, validated_data):
        movies = validated_data.pop('movie_id', [])
        genre = Genre.objects.create(**validated_data)

        for movie in movies:
            movie.genre = genre
            movie.save()
        return genre

    def update(self, instance, validated_data):
        movies = validated_data.pop('movie_ids', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if movies:
            for movie in movies:
                movie.genre = instance
                movie.save()

        return instance





