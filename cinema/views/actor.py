
from rest_framework.viewsets import ModelViewSet

from ..models import Actor
from ..serializers import ActorSerializer
from api.permissions import MyAuthenticatedOrReadOnly

class ActorAPIViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [MyAuthenticatedOrReadOnly]
