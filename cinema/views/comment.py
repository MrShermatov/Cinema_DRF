
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet

from api.permissions import CommentAuthor, MyAuthenticatedOrReadOnly
from ..models import Movie
from ..serializers.comment import CommentSerializer
from ..models import Comment


class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [CommentAuthor, MyAuthenticatedOrReadOnly]

    lookup_url_kwarg = 'comment_id'
    def get_queryset(self):
        return Comment.objects.filter(movie_id =self.kwargs.get('movie_id'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_id'))
        serializer.validated_data['user']  = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer
