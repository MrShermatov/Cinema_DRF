from rest_framework.viewsets import ModelViewSet
from ..models import Movie
from ..serializers import MovieReadSerializer, MovieWriteSerializer

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.select_related('genre', 'director').prefetch_related('actor')

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MovieReadSerializer
        return MovieWriteSerializer