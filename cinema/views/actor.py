from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Actor
from ..serializers import ActorSerializer

class ActorApiView(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveApiView(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer