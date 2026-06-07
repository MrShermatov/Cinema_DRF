from rest_framework.viewsets import ModelViewSet
from ..models import Movie
from ..serializers import MovieReadSerializer, MovieWriteSerializer

class MovieViewSet(ModelViewSet):

    def get_queryset(self):
        queryset = Movie.objects.select_related(
            'genre', 'director'
        ).prefetch_related('actor')

        genre_id = self.request.query_params.get('genre')
        if genre_id:
            queryset = queryset.filter(genre_id=genre_id)

        return queryset
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MovieReadSerializer
        return MovieWriteSerializer