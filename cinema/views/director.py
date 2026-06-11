from rest_framework.viewsets import ModelViewSet

from ..models import Director
from ..serializers import DirectorSerializer

class DirectorAPIViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
