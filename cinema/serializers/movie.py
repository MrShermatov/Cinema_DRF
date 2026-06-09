from ..models.movie import Movie
from rest_framework import serializers
from .actor import ActorSerializer
from .director import DirectorSerializer

class MovieReadSerializerForGenre(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description',
                  'release_year', 'image', 'director', 'actors']

class MovieReadSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    # genre = serializers.StringRelatedField(
    #     source='genre', read_only=True
    # )

    # genre = serializers.PrimaryKeyRelatedField(
    #     source='genre', read_only=True
    # )

    # genre = serializers.HyperlinkedRelatedField(
    #     source='genre', read_only=True,
    #     view_name='genre-detail'
    # )


    genre = serializers.SlugRelatedField(
        source='genre', read_only=True,
        slug_field='name'
    )


    url = serializers.HyperlinkedIdentityField(
        view_name='movie-detail'
    )
    class Meta:
        model = Movie
        fields = '__all__'

    def get_genre(self, obj):
        from .genre import GenreSerializer
        return GenreSerializer(obj.genre).data
    
class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        depth = 1
