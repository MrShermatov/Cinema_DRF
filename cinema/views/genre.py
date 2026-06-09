from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Genre
from ..serializers import GenreSerializer,GenreWriteSerializer

class GenreApiView(ListCreateAPIView):
    queryset = Genre.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return GenreWriteSerializer
        return GenreSerializer

class GenreRetrieveApiView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return GenreWriteSerializer
        return GenreSerializer
