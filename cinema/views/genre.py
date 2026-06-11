from rest_framework.viewsets import ModelViewSet

from ..models import Genre
from ..serializers import GenreSerializer,GenreWriteSerializer

class GenreAPIViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GenreWriteSerializer
        return GenreSerializer

