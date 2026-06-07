from django.db.models.fields import return_None
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from api.permissions import CommentAuthor, MyAuthenticatedOrReadOnly
from ..models import Movie
from ..serializers.comment import CommentSerializer
from ..models import Comment


class CommentApiview(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [CommentAuthor, MyAuthenticatedOrReadOnly]
    def get_queryset(self):
        return Comment.objects.filter(movie_id =self.kwargs.get('movie_id'))

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('movie_id'))
        serializer.validated_data['user']  = self.request.user
        serializer.validated_data['movie'] = movie
        serializer.save()
        return serializer

class CommentRetrieveApiView(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_id'
    permission_classes = [CommentAuthor, MyAuthenticatedOrReadOnly]
