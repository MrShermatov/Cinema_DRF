from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Actor
from ..serializers import ActorSerializer
from api.permissions import MyAuthenticatedOrReadOnly

class ActorApiView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [MyAuthenticatedOrReadOnly]

class ActorRetrieveApiView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [MyAuthenticatedOrReadOnly]